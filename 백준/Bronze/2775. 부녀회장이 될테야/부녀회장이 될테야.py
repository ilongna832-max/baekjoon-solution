a=int(input())
answer=[[0]*15 for _ in range(15)]
for i in range(1,len(answer)):
    answer[0][i]=i
for m in range(1,15):
    for n in range(1,15):
        answer[m][n]=answer[m][n-1]+answer[m-1][n]
for _ in range(a):
    k=int(input())
    n=int(input())
    print(answer[k][n])
