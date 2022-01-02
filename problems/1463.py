# https://www.acmicpc.net/problem/1463

import sys
import collections


input = sys.stdin.readline
res = collections.defaultdict(int)

N = int(input())

for i in range(2, N+1):
    res[i] = res[i-1] + 1

    if i % 2 == 0:
        res[i] = min(res[i], res[i//2]+1)

    if i % 3 == 0:
        res[i] = min(res[i], res[i // 3] + 1)

print(res[N])
