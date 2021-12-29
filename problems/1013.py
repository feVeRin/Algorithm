# https://www.acmicpc.net/problem/1013

import sys
import re

input = sys.stdin.readline
regex = re.compile(r'(100+1+|01)+')

n = int(input())
for _ in range(n):
    strs = str(input().rstrip())
    res = regex.fullmatch(strs)
    if res:
        print('YES')
    else:
        print('NO')
