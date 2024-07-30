import sys

input = sys.stdin.readline

N, K = map(int, input().split())

seq = list(range(1, N+1))
idx = K-1

print("<", end='')
for _ in range(N-1):
    print(seq.pop(idx), end=", ")
    idx = idx+K-1
    if idx>=len(seq):
        idx = idx%len(seq)

print(seq[0], ">", sep="")