import sys

input = sys.stdin.readline

N = int(input())
weights = []
for i in range(N):
    weights.append(list(map(int, input().split())))

answer = []
for idx1, weight1 in enumerate(weights):
    rank = 1
    x, y = weight1
    for idx2, weights2 in enumerate(weights):
        if idx1 == idx2:
            continue
        p, q = weights2
        if x<p and y<q:
            rank += 1
    answer.append(rank)
    
print(*answer)