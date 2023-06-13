import sys
input = sys.stdin.readline

chess = {'k':1, 'q':1, 'r':2, 'b':2, 'kn':2, 'p':8}
pieces = list(map(int, input().split()))
for c, p in zip(chess.values(), pieces):
    print(c-p, end=' ')