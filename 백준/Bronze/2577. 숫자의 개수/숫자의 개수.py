count=1
for _ in range(3):
    a=int(input())
    count*=a
total=str(count)
answer=[0]*10
for i in total:
    i=int(i)
    answer[i]+=1
for j in answer:
    print(j)