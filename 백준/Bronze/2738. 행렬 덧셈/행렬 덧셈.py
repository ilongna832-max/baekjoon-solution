import sys
input=sys.stdin.readline
a,b=map(int,input().split())
matrix_a=[]
matrix_b=[]
for _ in range(a):
    row=list(map(int,input().split()))
    matrix_a.append(row)
for _ in range(a):
    row1=list(map(int,input().split()))
    matrix_b.append(row1)
for i in range(a):
    answer=[]
    for j in range(b):
        total=matrix_a[i][j]+matrix_b[i][j]
        answer.append(total)
    print(*answer)