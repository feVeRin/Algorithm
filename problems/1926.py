import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ans = 0

def bfs(x, y):
    paint[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    count = 1
    queue = collections.deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m and paint[nx][ny] == 1:
                queue.append([nx, ny])
                paint[nx][ny] = 0
                count += 1
                
    return count

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt)
print(ans)