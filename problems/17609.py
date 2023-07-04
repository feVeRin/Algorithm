import sys
input = sys.stdin.readline

def ppalindrome(strings, left, right):
    while left < right:
        if strings[left] == strings[right]:
            left += 1
            right -= 1
        else:
            return 'no'
    return 'pesudo'

def palindrome(strings):
    left = 0
    right = len(strings)-1

    if strings == strings[::-1]:
        return 0

    while left < right:
        if strings[left] == strings[right]:
            left += 1
            right -= 1
        else:
            ppalin_left = ppalindrome(strings, left+1, right)
            ppalin_right = ppalindrome(strings, left, right-1)

            if 'pesudo' in [ppalin_left, ppalin_right]:
                return 1
            else:
                return 2

N = int(input())

for _ in range(N):
    strings = input().rstrip()
    print(palindrome(strings))