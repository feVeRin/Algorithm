from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque([])

def bfs():
	while queue:
		x, y, z = queue.popleft()
		for i in range(6):
			nx = x + dx[i]
			ny = y + dy[i]
			nz = z + dz[i]
			if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]:
				graph[nx][ny][nz] = graph[x][y][z] + 1
				queue.append([nx, ny, nz])

m, n, h = map(int, stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

for i in range(h):
	for j in range(n):
		for k in range(m):
			if graph[i][j][k] == 1:
				queue.append([i, j, k])
bfs()

answer = 0
for i in graph:
	for j in i:
		if 0 in j:
			print(-1)
			exit(0)
		answer = max(answer, max(j))
print(answer - 1)