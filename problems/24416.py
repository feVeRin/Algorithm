import sys
input = sys.stdin.readline
global count1
count1 = 0

def fibo1(n):
    global count1

    if n == 1 or n == 2:
        count1 += 1
        return 1
    else:
        count1 += 1
        return fibo1(n-1)+fibo1(n-2)

def fibo2(n):
    fibo = [0]*40
    count2 = 1
    fibo[0] = 1
    fibo[1] = 1
    for i in range(3, n):
        count2 += 1
        fibo[i] = fibo[i-1] + fibo[i-2]
    return count2

if __name__ == '__main__':
    N = int(input())

    x = fibo1(N)
    y = fibo2(N)
    print(x, y)