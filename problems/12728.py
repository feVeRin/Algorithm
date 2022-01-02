# https://www.acmicpc.net/problem/12728

import sys
from decimal import *

input = sys.stdin.readline


def calc(num):
    five = Decimal(5)
    getcontext().prec = 100
    return (3 + five.sqrt()) ** (num if num < 103 else (num - 3) % 100 + 3)


n = int(input())
for i in range(n):
    m = int(input())
    print("Case #{0}: {1:03d}".format(i+1, int(calc(m) % 1000)))
