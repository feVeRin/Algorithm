# https://www.acmicpc.net/problem/5893

import sys

input = sys.stdin.readline

N = str(input().rstrip())
binN = 0

for idx, n in enumerate(N[::-1]):
    if n == '1':
        binN += 2 ** idx

print(bin(binN*17)[2:])
