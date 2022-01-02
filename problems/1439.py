# https://www.acmicpc.net/problem/1439

import sys

input = sys.stdin.readline

strs = str(input().rstrip())
res = []

for i in range(len(strs)-1):
    if strs[i] != strs[i+1]:
        res.append(i+1)

if len(res) % 2:
    print(len(res)//2+1)
else:
    print(len(res)//2)
