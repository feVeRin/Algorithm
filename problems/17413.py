# https://www.acmicpc.net/problem/17413

import sys

input = sys.stdin.readline

strs = str(input().rstrip())
flag = False
res = ''
tmp = ''

for s in strs:
    if s == '<':
        flag = True
        res += tmp[::-1] + s
        tmp = ''
    elif s == '>':
        res += s
        flag = False
    elif s == ' ':
        if not flag:
            res += tmp[::-1] + s
            tmp = ''
        else:
            res += s
    else:
        if not flag:
            tmp += s
        else:
            res += s

res += tmp[::-1]
print(res)
