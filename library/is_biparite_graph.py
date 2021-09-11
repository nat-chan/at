#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *
from atcoder.dsu import DSU

def is_bipartite_graph(N: int, A: List[int], B: List[int]):
    """
    N: 頂点数、頂点番号0~N-1
    頂点A[i], B[i]に辺が貼られているとき
    二部グラフ判定をDSUを使って行う
    問題：https://atcoder.jp/contests/abc199/tasks/abc199_d
    解説：https://noshi91.hatenablog.com/entry/2018/04/17/183132
    """
    dsu = DSU(2*N)
    for a, b in zip(A, B):
        dsu.merge(2*a+0, 2*b+1)
        dsu.merge(2*a+1, 2*b+0)
    for a in range(N):
        if dsu.same(2*a+0, 2*a+1):
            return False
    return True