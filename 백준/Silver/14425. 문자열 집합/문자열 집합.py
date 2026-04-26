a,b=map(int,input().split())
c=set()
answer=[]
count=0
for _ in range(a):
    d=input()
    c.add(d)
for _ in range(b):
    data=input()
    answer.append(data)
for i in answer:
    if i in c:
        count+=1
print(count)

