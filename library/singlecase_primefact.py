#!/usr/bin/env python3
from typing import *
from functools import reduce

def div(n: int) -> List[int]:
    """
    O(logN √N)で上から抑えられてる
    """
    if n == 1: return [] # 1の素因数分解はうまく定義できない
    primes = list()
    while True:
        p = 2
        while p*p <= n:
            if n%p == 0:
                primes.append(p)
                n //= p
                break
            p += 1
        else:
            primes.append(n)
            return primes

def vid(arr: List[int]) -> int:
    """
    divの逆、リストの総積を取る
    """
    if arr == []: return 1
    return reduce(int.__mul__, arr)
