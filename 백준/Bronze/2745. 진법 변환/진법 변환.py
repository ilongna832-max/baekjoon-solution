a,b=map(str,input().split())
b=int(b)
total="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=a[::-1]
count=0
for i in range(len(a)):
    value=total.index(a[i])
    count+=value*(b**i)
print(count)