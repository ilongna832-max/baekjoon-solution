a,b=map(int,input().split())
count=1
while b>a:
    if b%2==0:
        b=b//2
    elif str(b)[-1]=='1':
        b=int(str(b)[:-1])
    else:
        break
    count+=1
if b==a:
    print(count)
else:
    print(-1)