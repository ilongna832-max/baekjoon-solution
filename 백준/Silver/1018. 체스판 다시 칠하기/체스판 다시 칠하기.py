import sys
input=sys.stdin.readline
n,m=map(int,input().split())
total=[input().strip() for _ in range(n)]
board=64
for i in range(0,n-7):
    for j in range(0,m-7):
        white=0
        black=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if total[a][b]!='W':
                        white+=1
                    if total[a][b]!='B':
                        black+=1    
                else:
                    if total[a][b]!='B':
                        white+=1
                    if total[a][b]!='W':
                        black+=1
        answer=min(white,black)        
        board=min(board,answer)
print(board)
