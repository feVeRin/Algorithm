# https://www.acmicpc.net/problem/1977

import sys
import math

input = sys.stdin.readline

M = int(input())
N = int(input())
res = []

for i in range(M, N+1):
    if i % math.sqrt(i) == 0:
        res.append(i)

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
