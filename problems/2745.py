import sys
import string
input = sys.stdin.readline

alpha = list(string.ascii_uppercase)
alpha_dict = dict()
for a, num in zip(alpha, range(10, 36)):
    alpha_dict[a] = num

N, B = input().split()

result = 0
for idx, n in enumerate(N[::-1]):
    adic = int(B) ** idx
    if n in alpha:
        result += alpha_dict[n] * adic
    else:
        result += int(n) * adic

print(result)