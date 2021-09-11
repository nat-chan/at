#!/usr/bin/env python3
from typing import *

class SparseMat:
    """
    疎な行列の積をMODを取りながら計算する。
    A = B@C
    A[i,j] = sum(B[i,k]*C[k,j] for k in range(N))
    A[i,j] を計算するときに
    B[i,・] の非零のkeysと
    C[・,j] の非零のkeysの積集合のみを渡ればよい。
    使用例: https://atcoder.jp/contests/typical90/submissions/23904417
    """
    MOD: int = 10**9+7
    def __init__(
        self,
        shape: Tuple[int, int],
        ) -> None:
        """
        numpy.zeros(shape)と同等の初期化
        """
        self.shape = shape
        self.H, self.W = shape
        self.h: List[Dict[int, int]] = [dict() for _ in range(self.H)]
        self.w: List[Dict[int, int]] = [dict() for _ in range(self.W)]
    def __getitem__(
        self,
        hw: Tuple[int, int],
        ) -> int:
        assert type(hw) == tuple and len(hw) == 2
        h, w = hw
        assert h in range(self.H) and w in range(self.W)
        in_h = w in self.h[h]
        in_w = h in self.w[w]
        assert in_h == in_w
        if in_h:
            val_h = self.h[h][w]
            val_w = self.w[w][h]
            assert val_h == val_w
            return val_h
        else:
            return 0
    def __setitem__(
        self,
        hw: Tuple[int, int],
        x: int
        ) -> None:
        assert type(hw) == tuple and len(hw) == 2
        h, w = hw
        assert h in range(self.H) and w in range(self.W)
        x %= self.MOD
        if x == 0:
            if w in self.h[h]:
                del self.h[h][w]
            if h in self.w[w]:
                del self.w[w][h]
        else:
            self.h[h][w] = x
            self.w[w][h] = x

    def _matmul(self, other, h, w):
        ans = 0
        for k in self.h[h].keys() & other.w[w].keys():
            ans += self.h[h][k]*other.w[w][k]
            ans %= self.MOD
        return ans

    def __matmul__(self, other):
        cls = type(self)
        assert cls == type(other)
        assert self.W == other.H
        retval = cls(shape=(self.H, other.W))
        for h in range(self.H):
            for w in range(other.W):
                retval[h, w] = self._matmul(other, h, w)
        return retval

    def __str__(self) -> str:
        txt = ""
        for h in range(self.H):
            for w in range(self.W):
                txt += f"{self[h, w]} "
            txt += "\n"
        return txt

def test_sm():
    import numpy as np
    for cls in [SparseMat, np.zeros]:
        B = cls(shape=(2, 3))
        B[0, 1] = 4
        B[1, 2] = 3
        C = cls(shape=(3, 2))
        C[2, 1] = 5
        C[1, 0] = 2
        A = B@C
        print(B)
        print(C)
        print(A)
