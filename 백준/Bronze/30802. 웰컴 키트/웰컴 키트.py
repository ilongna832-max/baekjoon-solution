a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
count=0
for i in b:
    count+=(i+c-1)//c
m,n=a//d,a%d
print(count)
print(m,n)