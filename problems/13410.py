# https://www.acmicpc.net/problem/13410

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
res = -sys.maxsize

for i in range(1, k+1):
    res = max(res, int(str(n*i)[::-1]))

print(res)
