num=list(map(int,input().split()))
count=0
for i in num:
    count+=i**2
print(count%10)