answer=[]
count=-1
for _ in range(9):
    row=list(map(int,input().split()))
    answer.append(row)
for i in range(9):
    for j in range(9):
        if answer[i][j]>count:
            count=answer[i][j]
            a=i+1
            b=j+1
print(count)
print(a,b)
