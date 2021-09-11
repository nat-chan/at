#!/usr/bin/env python3
from typing import *

def abs_nearest(A: List[int], x: int) -> Union[int, float]:
    """
    abs(A[i]-x)が最小となるA[i]を二分探索で返す
    時間計算量：O(logN)
    """
    if len(A) == 0: return float("inf")
    if len(A) == 1: return A[0]
    l = 0
    r = len(A)-1
    if x <= A[l]: return A[l]
    if not x <= A[r]: return A[r]
    while r-l>1:
        m = (l+r)//2
        if x <= A[m]:
            r = m
        else:
            l = m
    if abs(x-A[l]) < abs(x-A[r]):
        return A[l]
    else:
        return A[r]

def abs_nearest_naive(A: List[int], x: int) -> Union[int, float]:
    """
    時間計算量：O(N)
    """
    ans = float("inf")
    for a in A:
        if abs(a-x) < abs(ans-x):
            ans = a
    return ans

def test_abs_nearest():
    N = 100
    for i in range(N):
        for j in range(N):
            A = list(range(i))
            x = j
            assert abs_nearest(A, x) == abs_nearest_naive(A, x) 