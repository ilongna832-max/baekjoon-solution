a=int(input())
b=list(map(int,input().split()))
count=[]
dic={
}
for i in b:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
c=int(input())
d=list(map(int,input().split()))
for j in d:
    if j in dic:
        count.append(dic[j])
    else:
        count.append(0)
print(*count)