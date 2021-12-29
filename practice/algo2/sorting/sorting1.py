N = int(input())

num = []
for _ in range(N):
    num.append(int(input()))

for n in sorted(num, reverse=True):
    print(n, end=' ')
