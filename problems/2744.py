# https://www.acmicpc.net/problem/2744

import sys

input = sys.stdin.readline

strs = input().strip()
new = ''

for st in strs:
    if st.islower():
        new += st.upper()
    else:
        new += st.lower()

print(new)
