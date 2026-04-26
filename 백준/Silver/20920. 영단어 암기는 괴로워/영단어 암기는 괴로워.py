import sys
input=sys.stdin.readline
a,b=map(int,input().split())
dic={}
for _ in range(a):
    word=input().strip()
    if len(word)>=b:
        if word not in dic:
            dic[word]=1
        else:
            dic[word]+=1
total=list(dic.keys())
total.sort(key=lambda x:(-(dic[x]),-len(x),x))
print(*total,sep='\n')