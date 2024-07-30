import sys

input = sys.stdin.readline

def roundd(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

difficulty = []
N =int(input())

if N == 0:
    print(0)
else:
    
    for i in range(N):
        difficulty.append(int(input()))
        
    difficulty.sort()
    trim = roundd(N*0.15)
    
    if trim > 0:
        print(roundd(sum(difficulty[trim:-trim])/len(difficulty[trim:-trim])))
    else:
        print(roundd(sum(difficulty)/len(difficulty)))