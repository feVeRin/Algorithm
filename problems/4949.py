# https://www.acmicpc.net/problem/4949

import sys

input = sys.stdin.readline

while True:
    check = True
    stack = []
    strs = str(input().rstrip())
    if strs == '.':
        break

    for s in strs:
        if s in ['(', '[']:
            stack.append(s)
        elif s == ']':
            if not stack or stack.pop() != '[':
                check = False
                break
        elif s == ')':
            if not stack or stack.pop() != '(':
                check = False
                break

    if check and not stack:
        print('yes')
    else:
        print('no')
