#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    k3 = (n - 1) // 3
    k5 = (n - 1) // 5
    k15 = (n - 1) // 15
    s_mult = 3 * (k3 * (k3+1))//2 + 5 * (k5 * (k5+1))//2 - 15 * (k15 * (k15+1))//2
    print(int(s_mult))
    