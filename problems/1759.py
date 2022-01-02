# https://www.acmicpc.net/problem/1759

import sys
import itertools

input = sys.stdin.readline

l, c = map(int, input().split())
password = sorted(list(input().rstrip().split()))
vowel = ['a', 'e', 'i', 'o', 'u']


for combi in itertools.combinations(password, l):
    count = 0
    for c in combi:
        if c in vowel:
            count += 1

    if 1 <= count <= l-2:
        print(''.join(combi))
