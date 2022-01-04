# https://www.acmicpc.net/problem/2609

import sys

input = sys.stdin.readline


def gcd(n, m):
    while m:
        n = n % m
        n, m = m, n
    return n, m


N, M = map(int, input().split())
n, m = gcd(N, M)
print(n)
print(N*M//n)
