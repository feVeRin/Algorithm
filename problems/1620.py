import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict1 = dict()
dict2 = dict()

for i in range(N):
    pokemon = str(input().rstrip())
    dict1[i] = pokemon
    dict2[pokemon] = i

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dict1[int(question)-1])
    else:
        print(dict2[question]+1)    
