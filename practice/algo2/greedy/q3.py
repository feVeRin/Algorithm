N = str(input())

count1 = 0
count2 = 0

if N[0] == '1':
    count1 += 1
else:
    count2 += 1

for i in range(len(N)-1):
    if N[i] != N[i+1]:
        if N[i+1] == '1':
            count1 += 1
        else:
            count2 += 1

print(min(count1, count2))
