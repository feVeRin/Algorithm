import sys
import collections

input = sys.stdin.readline

maze = []
n, m = map(int, input().split())
for i in range(n):
    maze.append(list(map(int, input().rstrip())))

def bfs(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    queue = collections.deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    
    return maze[n-1][m-1]

print(bfs(0,0))