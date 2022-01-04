# https://www.acmicpc.net/problem/2774

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    strs = set(str(input().rstrip()))
    print(len(strs))
