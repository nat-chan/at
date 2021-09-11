#!/usr/bin/env python3

def outer(i):
    def inner(s):
        return f"\x1b[3{i}m{s}\x1b[m"
    return inner

for i, c in enumerate("rgybmc"):
    globals()[c] = outer(i+1)

if __name__ == "__main__":
    print(r("red"))
    print(g("green"))
    print(b("blue"))
    print(c("cyan"))
    print(m("magenta"))
    print(y("yellow"))