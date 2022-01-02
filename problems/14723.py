# https://www.acmicpc.net/problem/14723

import sys

input = sys.stdin.readline

N = int(input())
a, b, i = 0, 1, 1

while True:
    if a <= N < b:
        break

    a = b
    b += i
    i += 1

res1 = i-1
res2 = 1

for k in range(N-a):
    res1 -= 1
    res2 += 1

print(res1, res2)
