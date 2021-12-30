# https://www.acmicpc.net/problem/11399

import sys


result = 0
wait = 0
input = sys.stdin.readline

n = int(input())
time = sorted(list(map(int, input().split())))

if n == 1:
    print(time[0])
else:
    for i in range(n):
        result += (wait + time[i])
        wait += time[i]

    print(result)
