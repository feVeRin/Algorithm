# https://www.acmicpc.net/problem/13163

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    strs = list(map(str, input().split()))
    strs[0] = 'god'
    print(''.join(strs))
