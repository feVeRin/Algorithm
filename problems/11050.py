# https://www.acmicpc.net/problem/11050

import sys
from math import factorial

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    print(factorial(n) // (factorial(m) * factorial(n-m)))
