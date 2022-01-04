# https://www.acmicpc.net/problem/5789

import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    strs = str(input().rstrip())
    for i in range(len(strs)//2):
        if strs[i] == strs[len(strs)-1-i]:
            res = 'Do-it'
        else:
            res = 'Do-it-Not'

    print(res)
