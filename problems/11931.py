# https://www.acmicpc.net/problem/11931

import sys
print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True))
