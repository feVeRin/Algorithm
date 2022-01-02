# https://www.acmicpc.net/problem/1213


import sys

input = sys.stdin.readline

strs = str(input().rstrip())
count = [0 for _ in range(26)]

for s in strs:
    count[ord(s)-65] += 1

odd = 0
strs1 = ''
strs2 = ''

for i in range(26):
    if count[i] % 2 == 1:
        odd += 1
        strs1 += chr(i+65)
    strs2 += chr(i+65) * (count[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(strs2+strs1+strs2[::-1])
