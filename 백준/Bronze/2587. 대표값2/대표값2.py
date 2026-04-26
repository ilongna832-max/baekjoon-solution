answer=[]
for i in range(5):
    a=int(input())
    answer.append(a)
mean=sum(answer)/len(answer)
answer.sort()
print(int(mean))
print(answer[2])