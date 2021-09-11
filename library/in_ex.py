#!/usr/bin/env python3
from typing import *
from functools import reduce
from itertools import combinations

class InEx:
    def __init__(
        self,
        oracle: Callable[[int], int]
        ) -> None:
        self.oracle = oracle

    @staticmethod
    def bin2set(b: int) -> Tuple[int, ...]:
        # TODO もっと速い実装ができる
        return tuple(i for i, x in enumerate(reversed(bin(b)[2:])) if x == '1')
    @staticmethod
    def set2bin(s: Iterable[int]) -> int:
        if not s: return 0
        return reduce(int.__or__, map(lambda x: 1<<x, s))

    @staticmethod
    def sign(i: int) -> int:
        return (-1)**(i%2+1)

    def __call__(self, S: int) -> int:
        ans = 0
        b = self.bin2set(S)
        for i in range(1, len(b)+1):
            for c in combinations(b, i):
                ans += self.sign(i) * self.oracle(self.set2bin(c))
        return ans
