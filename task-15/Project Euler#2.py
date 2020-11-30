#!/bin/python3

import sys

def s_fib_even(n) :
    f, f1, f2, s = 0, 0, 2, 2
    while True:
        f = 4 * f2 + f1
        if (f > n) :
            break
        f1 = f2
        f2 = f
        s += f
    return s

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if (n > 1) :
        print(s_fib_even(n))
    else :
        print('0')