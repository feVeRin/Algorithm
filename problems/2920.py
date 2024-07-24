import sys

input = sys.stdin.readline

mode = list(map(int, input().split()))
asc = list(range(1,9))
des = list(range(8,0,-1))

if mode== asc:
    print('ascending')
elif mode==des:
    print('descending')
else:
    print('mixed')