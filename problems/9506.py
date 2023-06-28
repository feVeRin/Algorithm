import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break
    
    res = set()
    perfect = 0

    for i in range(1, N//2+1):
        if N % i == 0:
            res.add(i)
            res.add(N//i)
    
    res = sorted(res)

    if sum(res)-N == N:
        print(N, '=', end=' ')
        for i in res[:-1]:
            if i != res[-2]:
                print(i, '+ ', end = '')
            else:
                print(i)
    else:
        print(N, 'is NOT perfect.')
