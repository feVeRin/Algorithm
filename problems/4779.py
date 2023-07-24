import sys
input = sys.stdin.readline

def cantor(length):
    if length == 1:
        return '-'

    lines = cantor(length // 3)
    blank = ' ' * (length // 3) 
    return lines + blank + lines

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            print(cantor(3**N))
        except:
            break