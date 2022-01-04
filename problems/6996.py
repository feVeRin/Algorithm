# https://www.acmicpc.net/problem/6996

def anagram(st1, st2):
    if sorted(st1) == sorted(st2):
        return True
    else:
        return False


n = int(input())

for i in range(n):
    strs = list(map(str, input().split()))

    if anagram(strs[0], strs[1]):
        print(strs[0] + ' & ' + strs[1] + ' are anagrams.')
    else:
        print(strs[0] + ' & ' + strs[1] + ' are NOT anagrams.')
