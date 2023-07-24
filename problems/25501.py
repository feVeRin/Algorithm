import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global count 
    count += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input().rstrip()
        count = 0

        res = isPalindrome(S)
        print(res, count)