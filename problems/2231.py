# https://www.acmicpc.net/problem/2231

import sys

input = sys.stdin.readline

n = int(input())
flag = False

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    tmp = i + sum(nums)
    if tmp == n:
        print(i)
        flag = True
        break

if not flag:
    print(0)
