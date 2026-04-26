a,b,c=map(int,input().split())
answer=sorted([a,b,c])
total=answer[-1]
d=answer[0]+answer[1]
if d>total:
    print(sum(answer))
else:
    total=d-1
    print(d*2-1)