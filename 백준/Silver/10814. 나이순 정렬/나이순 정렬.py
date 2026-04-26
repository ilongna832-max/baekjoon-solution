a=int(input())
answer=[]
for _ in range(a):
    age,name=map(str,input().split())
    answer.append([int(age),name])
answer.sort(key=lambda x:x[0])
for i in answer:
    print(i[0],i[1])
