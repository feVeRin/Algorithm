# https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

n = int(input())

meeting = [list(map(int, input().split())) for _ in range(n)]
count = 0
time = 0

for t in sorted(meeting, key=lambda x: (x[1], x[0])):
    if t[0] >= time:
        time = t[1]
        count += 1

print(count)
