a=int(input())
answer=[]
for _ in range(a):
    b=list(map(int,input().split()))
    answer.append(b)
answer.sort(key=lambda x:(x[0],x[1]))
for i in answer:
    print(i[0],i[1])
