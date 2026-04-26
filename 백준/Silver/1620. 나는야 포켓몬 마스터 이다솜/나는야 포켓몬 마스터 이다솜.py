import sys
input=sys.stdin.readline
a,b=map(int,input().split())
name={}
number={}
count=1
for _ in range(a):
    c=input().strip()
    name[c]=count
    number[count]=c
    count+=1
for _ in range(b):
    d=input().strip()
    if d.isdigit():
        print(number[int(d)])
    else:
        print(name[d])
