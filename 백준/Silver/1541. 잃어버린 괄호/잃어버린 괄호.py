a=input().split('-')
answer=[]
for i in a:
    i=sum(map(int,i.split('+')))
    answer.append(i)
start=answer[0]
for i in range(1,len(answer)):
    start-=answer[i]
print(start)
    
        
