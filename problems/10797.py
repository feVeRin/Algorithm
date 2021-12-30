# https://www.acmicpc.net/problem/10797

import sys

input = sys.stdin.readline

day = int(input())
cars = list(map(int, input().split()))
count = 0

for car in cars:
    if car == day:
        count += 1

print(count)
