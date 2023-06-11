import sys
input = sys.stdin.readline

N = int(input())
xlist = list(map(int, input().split()))
keys = sorted(set(xlist))
shirink = {}

for i in range(len(keys)):
    shirink[keys[i]] = i

for x in xlist:
    print(shirink[x], end=' ')