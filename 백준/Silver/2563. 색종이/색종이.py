total=[[0]*100 for _ in range(100)]
a=int(input())
count=0
for _ in range(a):
    b,c=map(int,input().split())
    for i in range(b,b+10):
        for j in range(c,c+10):
            total[i][j]=1
for row in total:
    count+=sum(row)
print(count)

    