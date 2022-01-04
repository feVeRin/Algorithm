# https://www.acmicpc.net/problem/2475

import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))
res = 0

for n in nums:
    res += n ** 2

print(res % 10)
