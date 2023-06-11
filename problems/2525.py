import sys
input = sys.stdin.readline

def convert(x):
    h = x // 60
    m = x % 60

    return h, m

def calc(h, m):
    if m > 59:
        h += 1
        m -= 60
    
    if h > 23:
        h -= 24
    
    return h, m    

if __name__ == '__main__':
    H, M = map(int, input().split())
    time = int(input())

    cvt_h, cvt_m = convert(time)
    
    h, m = calc(H+cvt_h, M+cvt_m)
    print(h, m)