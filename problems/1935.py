# https://www.acmicpc.net/problem/1935

import sys
import collections

input = sys.stdin.readline

n = int(input())
expression = list(str(input().rstrip()))
num = collections.defaultdict(int)
stack = []

for i in range(n):
    num[i] = int(input())

for e in expression:
    if e.isalpha():
        stack.append(num[ord(e)-ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        aeb = str(a)+e+str(b)
        stack.append(eval(aeb))

print('{:.2f}'.format(stack.pop()))
