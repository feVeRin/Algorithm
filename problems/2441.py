# https://www.acmicpc.net/problem/2441

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n, 0, -1):
    star = ' '*(n-i) + '*'*i
    print(star)
