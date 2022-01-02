# https://www.acmicpc.net/problem/1964

import sys

input = sys.stdin.readline

n = int(input())
res = ((3*n**2 + 5*n) // 2) + 1
print(res % 45678)
