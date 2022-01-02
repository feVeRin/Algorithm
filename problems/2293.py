# https://www.acmicpc.net/problem/2293

import sys
import collections

input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

tb = collections.defaultdict(int)
tb[0] = 1

for c in coin:
    for i in range(c, K + 1):
        tb[i] += tb[i - c]

print(tb[K])
