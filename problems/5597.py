# https://www.acmicpc.net/problem/5597

import sys

input = sys.stdin.readline

students = [0] * 30

for _ in range(28):
    n = int(input())
    students[n-1] = 1

for idx, check in enumerate(students):
    if check == 0:
        print(idx+1)
