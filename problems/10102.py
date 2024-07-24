import sys
import collections

input = sys.stdin.readline

n=int(input())
vote = input().rstrip()

counter = collections.Counter(vote)
a_counter = counter['A']
b_counter = counter['B']

if a_counter > b_counter:
    print('A')
elif b_counter > a_counter:
    print('B')
else:
    print('Tie')