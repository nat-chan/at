#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import *

def subset(bit: int) -> Iterable[int]:
    """
    入力: 要素数Nの集合を立っているビットで管理したint
    出力: bitのすべての部分集合を渡るIterable[int]
    for bit in range(1<<N)に対してこの関数を呼んだ場合
    \sum_{k=N}^{N} N_C_k 2^k = (1+2)^N = 3^Nより
    時間計算量: O(3^N)
    """
    sub = bit
    while 0 < sub:
        yield sub
        sub = (sub-1)&bit
