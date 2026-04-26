a,b=map(int,input().split())
answer=[]
for i in range(1,a+1):
    answer.append(i)
for j in range(b):
    c,d=map(int,input().split())
    number=answer[c-1:d]
    number.reverse()
    answer[c-1:d]=number
print(*answer)