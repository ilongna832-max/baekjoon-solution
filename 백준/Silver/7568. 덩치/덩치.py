a=int(input())
rank=1
answer=[]
for _ in range(a):
    m,n=map(int,input().split())
    answer.append([m,n])
rank=[]
for i in range(a):
    count=1
    for j in range(a):
        if answer[i][0]<answer[j][0] and answer[i][1]<answer[j][1]:
            count+=1
    rank.append(count)     
print(*rank)