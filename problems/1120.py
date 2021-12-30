# https://www.acmicpc.net/problem/1120

import sys

input = sys.stdin.readline

a, b = input().split()
res = sys.maxsize

for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1

    res = min(res, count)

print(res)
