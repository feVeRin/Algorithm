import sys
input = sys.stdin.readline

dance = {'ChongChong'}
N = int(input())
for _ in range(N):
    a, b = input().split()
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))