a=int(input())
b=0
start=max(1,a-54)
for i in range(start,a):
    count=i
    for j in str(i):
        count+=int(j)
    if count==a:
        b=i
        print(i)
        break
if b==0:
    print(0)