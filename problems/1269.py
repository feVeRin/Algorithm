import sys
input = sys.stdin.readline

N, M = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

AB = len(set_A.difference(set_B))
BA = len(set_B.difference(set_A))
print(AB+BA)