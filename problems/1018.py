import sys
input = sys.stdin.readline

chess = []
chess2 = []
N, M = map(int, input().split())

for _ in range(N):
    chess.append(list(input().rstrip()))

for row in range(N-7):
    for col in range(M-7):
        white = 0
        black = 0
        
        for r in range(row, row+8):
            for c in range(col, col+8):
                if (r+c)%2 == 0:
                    if chess[r][c] != 'W': 
                        white += 1  
                    else:
                        black += 1
                else:
                    if chess[r][c] != 'W': 
                        black += 1  
                    else:
                        white += 1
        chess2.append(white)
        chess2.append(black)

print(min(chess2))       
