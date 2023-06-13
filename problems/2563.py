import sys
from collections import Counter
input = sys.stdin.readline

paper = [[0 for _ in range(101)] for _ in range(101)]
result = 0
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for p in paper:
    result += p.count(1)

print(result)