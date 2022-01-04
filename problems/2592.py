# https://www.acmicpc.net/problem/2592

import sys

input = sys.stdin.readline
num = [int(input()) for _ in range(10)]

print(sum(num)//10)
print(max(num, key=num.count))
