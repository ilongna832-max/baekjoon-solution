a,b=map(int,input().split())
answer=[]
for i in range(1,a+1):
    if a%i==0:
        answer.append(i)  
if len(answer)>=b:
    print(answer[b-1])
else:
    print(0)