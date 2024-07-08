import sys
import collections

input = sys.stdin.readline

tomatos = []
start = []

m,n = map(int, input().split())
for _ in range(n):
    tomatos.append(list(map(int, input().split())))
    
for i, row in enumerate(tomatos):
    for j, tomato in enumerate(row):
        if tomato==1:
            start.append([i,j])
            
def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = collections.deque(start)
    
    while queue:
        xx, yy = queue.popleft()

        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
        
            if 0<=nx<n and 0<=ny<m and tomatos[nx][ny]==0:
                tomatos[nx][ny] = tomatos[xx][yy]+1
                queue.append([nx,ny])

bfs()
res = 0  
flag = True
for row in tomatos:
    for tomato in row:
        if tomato == 0:
            flag=False
    res = max(res, max(row))

if flag:
    print(res - 1)
else:
    print(-1)