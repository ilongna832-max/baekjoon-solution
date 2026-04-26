a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
count=0
for i in range(a):
    count+=b[i]*c[i]
print(count)