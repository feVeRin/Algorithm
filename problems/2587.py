# https://www.acmicpc.net/problem/2587

import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(5)]
print(sum(nums) // 5)
print(sorted(nums)[2])
