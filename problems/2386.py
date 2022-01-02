# https://www.acmicpc.net/problem/2386

import sys
import collections

input = sys.stdin.readline

while True:
    strs = str(input().rstrip().lower())
    if strs == '#':
        break

    check = True
    alpha, sentence = strs[0], strs[1:].strip()
    counter = collections.Counter(sentence)
    for c in counter:
        if c == alpha:
            print(alpha, counter[c])
            check = False
            break

    if check:
        print(alpha, 0)
