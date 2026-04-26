a=int(input())
row=[]
column=[]
for _ in range(a):
    x,y=list(map(int,input().split()))
    row.append(x)
    column.append(y)
total=max(row)-min(row)
answer=max(column)-min(column)
print(total*answer)