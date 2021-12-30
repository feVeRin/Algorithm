# https://www.acmicpc.net/problem/11721

import sys

input = sys.stdin.readline
strs = str(input().rstrip())

for i in range(0, len(strs), 10):
    print(strs[i:i+10])
