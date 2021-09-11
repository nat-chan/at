#!/usr/bin/env python3
from subprocess import Popen, PIPE, TimeoutExpired
import sys


class Align:
    def __enter__(self):
        self.proc = Popen(
            "column -t",
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            shell=True,
            text=True
        )
        self.__stdout__ = sys.stdout
        sys.stdout = self.proc.stdin
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        sys.stdout = self.__stdout__
        try:
            outs, errs = self.proc.communicate(timeout=15)
        except TimeoutExpired:
            self.proc.kill()
            outs, errs = self.proc.communicate()
        print(outs, end="", file=sys.stdout)
        print(errs, end="", file=sys.stderr)


def test_Align():
    N = 12
    index = list(range(N))
    parity = [i%2 for i in range(N)]
    print("start")
    with Align():
        print("index", *index)
        print("parity", *parity)
    print("end")
    """以下のように整列されて表示される
    start
    index   0  1  2  3  4  5  6  7  8  9  10  11
    parity  0  1  0  1  0  1  0  1  0  1  0   1
    end
    """

if __name__ == '__main__':
    test_Align()