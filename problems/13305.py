# https://www.acmicpc.net/problem/13305

import sys

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

res = 0
mp = sys.maxsize

for i in range(len(price)-1):
    mp = min(mp, price[i])
    res += mp * road[i]

print(res)
