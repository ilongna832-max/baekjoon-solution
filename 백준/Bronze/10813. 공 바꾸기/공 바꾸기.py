a,b=list(map(int,input().split()))
answer=[]
for i in range(1,a+1):
    answer.append(i)
for j in range(b):
    c,d=list(map(int,input().split()))
    c=c-1
    d=d-1
    answer[c],answer[d]=answer[d],answer[c]
for i in answer:
    print(i,end=' ')