a,b=map(int,input().split())
c=set(map(int,input().split()))
d=set(map(int,input().split()))
total=[]
for i in c:
    if i in d:
        total.append(i)
count1=len(c)-len(total)
count2=len(d)-len(total)
print(count1+count2)
        