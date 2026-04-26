a=int(input())
b=[300,60,10]
answer=[]
for i in b:
    remain=a//i
    a%=i
    answer.append(remain)
if a!=0:
    print(-1)
else:
    print(*answer)
