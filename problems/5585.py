# https://www.acmicpc.net/problem/5585

price = 1000 - int(input())

coin = [500, 100, 50, 10, 5, 1]
res = 0

for c in coin:
    res += price // c
    price %= c
    if price == 0:
        break

print(res)
