a,b=map(int,input().split())
total=a*60+b-45
if total<0:
    total+=24*60
c=total//60
d=total%60
print(c,d)