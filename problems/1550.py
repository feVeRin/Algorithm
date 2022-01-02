# https://www.acmicpc.net/problem/1550

import sys

input = sys.stdin.readline

hexa = str(input().rstrip())
match = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
res = 0

for idx, h in enumerate(hexa[::-1]):
    if h in match:
        h = match[h]

    res += int(h) * (16**idx)

print(res)
