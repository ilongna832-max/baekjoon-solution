a=int(input())
b=set(map(int,input().split()))
c=int(input())
answer=list(map(int,input().split()))
total=[1 if i in b else 0 for i in answer]
print(*total)