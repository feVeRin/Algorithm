# https://www.acmicpc.net/problem/1541

import sys

input = sys.stdin.readline

expression = input().strip().split('-')
res = 0

for exp in expression[0].split('+'):
    res += int(exp)

for exp in expression[1:]:
    for ex in exp.split('+'):
        res -= int(ex)

print(res)

