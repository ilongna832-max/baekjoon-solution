import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=list(map(int,input().split()))
total=[0]
count=0
for i in c:
    count+=i
    total.append(count)
for _ in range(b):
    start,stop=map(int,input().split())
    print(total[stop]-total[start-1])
    