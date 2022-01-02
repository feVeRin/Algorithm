# https://www.acmicpc.net/problem/18406

import sys

input = sys.stdin.readline

num = str(input().rstrip())
partition = len(num) // 2
num = [int(n) for n in num]

if sum(num[:partition]) == sum(num[partition:]):
    print('LUCKY')
else:
    print('READY')
