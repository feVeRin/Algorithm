# https://www.acmicpc.net/problem/1874


import sys

input = sys.stdin.readline

n = int(input())
stack, tmp = [], []
d = 1

for i in range(n):
    data = int(input())

    while d <= data:
        stack.append(d)
        tmp.append('+')
        d += 1

    if stack[-1] == data:
        stack.pop()
        tmp.append('-')
    else:
        break

if stack:
    print('NO')
else:
    for t in tmp:
        print(t)
