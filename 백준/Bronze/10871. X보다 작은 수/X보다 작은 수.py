a=input().split()
if a:
    data=int(a[1])
b=list(map(int, input().split()))
for i in range(len(b)):
    if b[i]<data:
        print(b[i],end=' ')