# https://www.acmicpc.net/problem/2576

import sys

input = sys.stdin.readline
num = [int(input()) for _ in range(7)]
odd = []

for n in num:
    if n % 2 != 0:
        odd.append(n)

if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))
