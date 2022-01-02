# https://www.acmicpc.net/problem/1212

import sys

input = sys.stdin.readline

octa = str(input().rstrip())
print(bin(int(octa, 8))[2:])
