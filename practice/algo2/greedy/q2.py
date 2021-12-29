S = str(input())

res = int(S[0])

for i in range(1, len(S)):
    n = int(S[i])
    if n <= 1 or res <= 1:
        res += n
    else:
        res *= n

print(res)
