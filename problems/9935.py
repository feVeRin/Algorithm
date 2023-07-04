import sys
from collections import deque
input = sys.stdin.readline

strings = list(input().rstrip())
explode = list(input().rstrip())
stack = []

for i in range(len(strings)):
    stack.append(strings[i])
    if stack[-1] == explode[-1] and len(stack) >= len(explode):
        if stack[-len(explode):] == explode:
            del stack[-len(explode):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
