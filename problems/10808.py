# https://www.acmicpc.net/problem/10808

word = input()
check = [0]*26

for w in word:
    check[ord(w)-97] += 1

for i in check:
    print(i, end=' ')
