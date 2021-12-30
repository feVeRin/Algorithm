# https://www.acmicpc.net/problem/11179

import sys

input = sys.stdin.readline

n = int(input())
binary = bin(n)[2:]
res = 0

for idx, b in enumerate(binary):
    if b == 0:
        continue
    else:
        res += int(b) * (2 ** idx)

print(res)
