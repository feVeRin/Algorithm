import sys
from collections import Counter
input = sys.stdin.readline

dices = list(map(int, input().split()))
counter = Counter(dices)

if 3 in counter.values():
    prize = 10000 + dices[0]*1000
elif 2 in counter.values():
    prize = 1000 + counter.most_common()[0][0]*100
else:
    prize = max(dices)*100

print(prize)
