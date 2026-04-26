import sys
input=sys.stdin.readline
a=int(input())
b=set()
for _ in range(a):
    c,d=input().split()
    if d=='leave':
        b.remove(c)
    else:
        b.add(c)
answer=sorted(b,reverse=True)
for i in answer:
    print(i)
