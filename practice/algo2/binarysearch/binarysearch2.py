N, M = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = max(num)
res = 0

while start <= end:
    tot = 0
    mid = (start+end) // 2

    for x in num:
        if x > mid:
            tot += x - mid

    if tot < M:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
