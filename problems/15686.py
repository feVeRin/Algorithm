# https://www.acmicpc.net/problem/15686

import sys
import itertools


input = sys.stdin.readline

n, m = map(int, input().split())
chicken, house = [], []


for i in range(n):
    info = list(map(int, input().split()))

    for j in range(n):
        if info[j] == 1:
            house.append((i, j))
        elif info[j] == 2:
            chicken.append((i, j))

combination = list(itertools.combinations(chicken, m))
res = sys.maxsize

for combi in combination:
    dist = 0
    for x, y in house:
        tmp = sys.maxsize
        for xx, yy in combi:
            tmp = min(tmp, abs(x - xx) + abs(y - yy))
        dist += tmp
    res = min(res, dist)

print(res)
