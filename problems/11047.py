# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
res = 0

for _ in range(N):
    coin.append(int(input()))

for c in sorted(coin, reverse=True):
    if K == 0:
        break

    res += K // c
    K %= c

print(res)
