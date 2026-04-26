a=int(input())
answer=[]
for i in range(2,a+1):
    while a%i==0:
        answer.append(i)
        a=a//i
for j in answer:
    print(j)