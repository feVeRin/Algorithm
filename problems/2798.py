import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

C = len(cards)
bj = 0

for c1 in range(0, C-2):
    for c2 in range(c1+1, C-1):
        for c3 in range(c2+1, C):
            tmp = cards[c1] + cards[c2] + cards[c3]
            if tmp <= M:
                bj = max(bj, tmp)

print(bj)
