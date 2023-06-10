import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
count = 0
for _ in range(N):
    string = str(input().rstrip())
    S.add(string)

for _ in range(M):
    string = str(input().rstrip())
    if string in S:
        count += 1

print(count)
