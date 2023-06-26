import sys
import string
input = sys.stdin.readline

alpha = list(string.ascii_uppercase)
alpha_dict = dict()
for a, num in zip(alpha, range(10, 36)):
    alpha_dict[num] = a

N, B = map(int, input().split())

result = ''
while N:
    mod = N % B
    if mod in range(10, 36):
        result += alpha_dict[mod]
    else:
        result += str(mod)
    N = N // B

print(result[::-1])