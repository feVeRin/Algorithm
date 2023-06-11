import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(N):
    set1.add(input().rstrip())

for _ in range(M):
    set2.add(input().rstrip()) 

result = sorted(set1.intersection(set2))
print(len(result))
for r in result:
    print(r)