import sys
import collections

input = sys.stdin.readline

n=int(input())
a,b = map(int, input().split())
m=int(input())

family = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

visited = [False for _ in range(n+1)]
def dfs(x, count):
    global flag
    visited[x] = True
    if x==b:
        flag=True
        print(count)
    for val in family[x]:
        if visited[val] == False:
            dfs(val,count+1)

flag=False
dfs(a,0)
if flag==False:
    print(-1)