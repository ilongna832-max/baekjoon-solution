a=int(input())
score=list(map(int,input().split()))
b=max(score)
for i in range(a):
    score[i]=(score[i]/b)*100
average=sum(score)/len(score)
print(average)
    