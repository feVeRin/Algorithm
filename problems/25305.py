import sys
input = sys.stdin.readline

N, K = map(int, input().split())
values = sorted(list(map(int, input().split())), reverse=True)

print(values[K-1])