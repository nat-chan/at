#!/usr/bin/env python3
# %%
from math import *
import unittest

# %%
def pow_msb(N, x):
    ans = 1
    for i in f"{N:b}":
        ans *= ans
        if i == '1': ans *= x
    return ans
# %%
def pow_lsb(N, x):
    ans = 1
    for i in f"{N:b}"[::-1]:
        if i == '1': ans *= x
        x *= x 
    return ans

# %%
class MyTest(unittest.TestCase):
    def test_pow_msb(self):
        for N in range(10):
            for x in range(10):
                self.assertEqual(
                    int(pow(x, N)),
                    pow_msb(N, x)
                )

    def test_pow_lsb(self):
        for N in range(10):
            for x in range(10):
                self.assertEqual(
                    int(pow(x, N)),
                    pow_lsb(N, x)
                )

    def test_error(self):
        self.assertEqual(0,1)

# %%
if __name__ == "__main__":
    unittest.main()
# %%
# %%
