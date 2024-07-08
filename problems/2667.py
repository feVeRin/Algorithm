import collections
import sys

input = sys.stdin.readline
    
def bfs(graph, x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = collections.deque()
    queue.append([x,y])
    graph[x][y]= 0
    count = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append([nx,ny])
                count+=1
    return count

graph = []
n=int(input())
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
    
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            tmp = bfs(graph, i,j)
            res.append(tmp)

print(len(res))
for i in sorted(res):
    print(i)
    