n, m = map(int, input().split())

cards = []
for _ in range(n):
    num = map(int, input().split())
    cards.append(num)

res = []

for row in cards:
    res.append(min(row))

print(max(res))
