import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
result = 0

for n in numbers:
    if v == n:
        result += 1

print(result)
