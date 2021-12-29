N, M = map(int, input().split())
balls = list(map(int, input().split()))

res = 0

# isn't it brute-force ?
for i in range(len(balls)):
    for j in range(i+1, len(balls)):
        if balls[i] == balls[j]:
            continue
        else:
            res += 1

print(res)
