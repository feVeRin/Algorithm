import sys
input = sys.stdin.readline

while True:
    num = list(map(int, input().split()))
    if num == [0, 0]:
        break

    if num[1] > num[0]:
        if num[1] % num[0] == 0:
            print('factor')
        else:
            print('neither')
    elif num[1] < num[0]:
        if num[0] % num[1] == 0:
            print('multiple')
        else:
            print('neither')
    else:
        print('neither')