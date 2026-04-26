a,b,c=map(int,input().split())
total=[a,b,c]
count=0
if a==b and b==c:
    count=10000+1000*b
elif a==b or b==c:
    count=1000+b*100
elif a==c:
    count=1000+a*100
else:
    count=max(total)*100
print(count)