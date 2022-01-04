# https://www.acmicpc.net/problem/3059

import sys
import string

input = sys.stdin.readline

n = int(input())
alpha = list(string.ascii_uppercase)

for _ in range(n):
    strs = str(input().rstrip())
    tmp = [0 for _ in range(len(alpha))]
    res = 0

    for s in strs:
        if s in alpha:
            tmp[ord(s)-ord('A')] += 1

    for i in range(len(alpha)):
        if tmp[i] == 0:
            res += i+ord('A')

    print(res)
