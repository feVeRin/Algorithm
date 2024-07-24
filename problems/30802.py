import sys

input = sys.stdin.readline

n= int(input())
size = list(map(int, input().split()))
t, p=map(int, input().split())

count = 0

for sz in size:
    count += sz//t
    if sz%t != 0:
        count += 1

print(count)
print(n // p, n % p)