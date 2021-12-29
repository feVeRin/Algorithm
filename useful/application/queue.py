# https://www.acmicpc.net/problem/10845

import sys

input = sys.stdin.readline
n = int(input())
q = []

for i in range(n):
    strs = input().split()
    if strs[0] == 'push':
        q.append(strs[1])
    elif strs[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif strs[0] == 'size':
        print(len(q))
    elif strs[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif strs[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif strs[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])



