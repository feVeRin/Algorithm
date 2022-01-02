# https://www.acmicpc.net/problem/1264

import sys

input = sys.stdin.readline
word = str(input())
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for w in word:
    if w in vowel:
        count += 1

print(count)
