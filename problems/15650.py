import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def backtracking(start):
    if len(res) == m:
        print(*res)
        return
    
    for i in range(start, n+1):
        if i not in res:
            res.append(i)
            backtracking(i+1)
            res.pop()

backtracking(1)