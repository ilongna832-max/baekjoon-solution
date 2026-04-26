a=list(map(int,input().split()))
b=[1,1,2,2,2,8]
answer=[]
for i in range(len(a)):
    count=b[i]-a[i]
    answer.append(str(count))
print(' '.join(answer))
    