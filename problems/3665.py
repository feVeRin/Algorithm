# https://www.acmicpc.net/problem/3665

import sys
import collections

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    ranks = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[ranks[i]][ranks[j]] = True
            indegree[ranks[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    res = []
    Q = collections.deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            Q.append(i)

    check = True
    cycle = False

    for i in range(n):
        if len(Q) == 0:
            cycle = True
            break
        if len(Q) >= 2:
            check = False
            break

        pop = Q.popleft()
        res.append(pop)
        for j in range(1, n+1):
            if graph[pop][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    Q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not check:
        print('?')
    else:
        for r in res:
            print(r, end=' ')
        print()
