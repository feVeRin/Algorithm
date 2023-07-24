import sys
input = sys.stdin.readline
 
T = int(input())
 
for _ in range(T):
    result = sys.maxsize
    N = int(input())
    mbtis = list(map(str, input().split()))

    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    count = 0
                    if i == j or j == k or i == k:
                        continue

                    for m in range(4):
                        if mbtis[i][m] != mbtis[j][m]: 
                            count += 1
                        if mbtis[j][m] != mbtis[k][m]: 
                            count += 1
                        if mbtis[i][m] != mbtis[k][m]: 
                            count += 1
                    result = min(result, count)
        print(result)