import sys
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    
    importance = list(map(int,input().split()))
    document = [x for x in range(len(importance))]
    
    count= 0
    
    while True:
        if importance[0] >= max(importance):
            count += 1
            if document[0] == M:
                break
            else:
                importance = importance[1:]
                document = document[1:]
        else:
            importance = importance[1:] + importance[:1]
            document = document[1:] + document[:1]
    print(count)
