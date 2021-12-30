# https://www.acmicpc.net/problem/10930

import hashlib
import sys

input = sys.stdin.readline

s = str(input().rstrip())
print(hashlib.sha256(s.encode()).hexdigest())
