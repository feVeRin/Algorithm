import sys
from collections import Counter
input = sys.stdin.readline

words = []
N, M = map(int, input().split())

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

counter = Counter(words)
for w, c in sorted(counter.most_common(), key= lambda x: (-x[1], -len(x[0]), x[0])):
    print(w)