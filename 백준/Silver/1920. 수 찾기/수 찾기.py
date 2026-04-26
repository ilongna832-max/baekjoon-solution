a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
for i in d:
    if i not in b:
        print(0)
    else:
        print(1)