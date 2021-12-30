# https://www.acmicpc.net/problem/10886

import sys


input = sys.stdin.readline
n = int(input())
cute = []

for _ in range(n):
    cute.append(int(input()))

if cute.count(0) > cute.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
