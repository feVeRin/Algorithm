import sys
input = sys.stdin.readline

def majority_vote(arr):
    count, major = 0, 0
    for a in arr:
        if count==0:
            major = a
        if major==a:
            count+=1
        else:
            count-=1
            
    k = len(arr)
    m = 0
    
    for a in arr:
        if a==major:
            m+=1
    if m>k//2:
        return major
    else:
        return "SYJKGW"
    
N = int(input())
for _ in range(N):
    soldier = list(map(int, input().split()))
    print(majority_vote(soldier[1:]))