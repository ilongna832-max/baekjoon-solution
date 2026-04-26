a=int(input())
data=list(map(int,input().split()))
answer=sorted(set(data))
dic={}
for i,v in enumerate(answer):
    dic[v]=i
for j in data:
    print(dic[j],end=' ')
        