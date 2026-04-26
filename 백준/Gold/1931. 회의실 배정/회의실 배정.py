a=int(input())
answer=[]
for _ in range(a):
    b,c=map(int,input().split())
    answer.append((b,c))
answer.sort(key=lambda x: (x[1],x[0]))
count=0
max_time=0
for start,end in answer:
    if start>=max_time:
        count+=1
        max_time=end
print(count)