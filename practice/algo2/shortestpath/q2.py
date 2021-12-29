import heapq

INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(int(input())):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dist = [[INF]*n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    dist[x][y] = graph[x][y]

    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = d+graph[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(dist[n-1][n-1])
