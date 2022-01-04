# https://www.acmicpc.net/problem/2857

import sys
import re

input = sys.stdin.readline
flag = False

for i in range(5):
    agent = str(input().rstrip())
    regex = re.search('FBI', agent)
    if regex:
        print(i+1)
        flag = True

if not flag:
    print('HE GOT AWAY!')
