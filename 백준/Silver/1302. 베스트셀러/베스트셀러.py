a=int(input())
dic={}
for _ in range(a):
    b=input()
    if b in dic:
        dic[b]+=1
    else:
        dic[b]=1
print(max(sorted(dic.keys()),key=dic.get))