answer=[]
for i in range(9):
    a=int(input())
    answer.append(a)
a=max(answer)
print(a)
print(answer.index(a)+1)