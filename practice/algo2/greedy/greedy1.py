n, m, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort()
res = 0
count = 0

for _ in range(m):
    for j in range(k):
        if count == m:
            break
            
        res += num[n-1]
        count += 1

    if count == m:
        break

    res += num[n-2]
    count += 1

print(res)
