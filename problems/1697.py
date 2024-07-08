import sys
import collections

input = sys.stdin.readline

n, k= map(int, input().split())
line = [0]*100001

def bfs(line, start, end):
    queue = collections.deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        if cur == end:
            return line[end]
        
        for nx in [cur+1, cur-1, cur*2]:
            if 0<=nx<100001 and not line[nx]:
                line[nx]=line[cur]+1
                queue.append(nx)

print(bfs(line, n, k))
