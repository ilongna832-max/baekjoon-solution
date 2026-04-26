a,b=map(int,input().split())
c=int(input())
d=int(input())
if a*d+b<=c*d and c>=a:
    print(1)
else:
    print(0)