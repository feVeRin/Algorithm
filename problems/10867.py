# https://www.acmicpc.net/problem/10867

n = int(input())

a = map(int, input().split())

for i in sorted(list(set(a))):
    print(i, end=' ')
