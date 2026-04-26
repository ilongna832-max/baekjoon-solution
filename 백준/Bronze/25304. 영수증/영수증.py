a=int(input())
b=int(input())
count=0
for i in range(b):
    c,d=map(int,input().split())
    count+=c*d
if a==count:
    print('Yes')
else:
    print('No')
