import sys
input=sys.stdin.readline
a=int(input())
dic={}
for _ in range(a):
    b=int(input())
    if b in dic:
        dic[b]+=1
    else:
        dic[b]=1
total=[]
answer=max(dic.values())
for i,v in dic.items():
    if v==answer:
        total.append(i)
print(min(total))