import sys

input = sys.stdin.readline

L = int(input())
strings = input().rstrip()

r = 31
m = 1234567891

hash = 0
for idx, st in enumerate(strings):
    a = ord(st)-96
    hash += a*(r**idx)
    
print(hash%m)