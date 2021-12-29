N = int(input())
fear = list(map(int, input().split()))
fear.sort()

res = 0
count = 0

for f in fear:
    count += 1
    if count >= f:
        res += 1
        count = 0

print(res)
