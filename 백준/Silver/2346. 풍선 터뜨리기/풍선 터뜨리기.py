from collections import deque
a=int(input())
queue=deque()
answer=[]
orders=map(int,input().split())
for i,order in enumerate(orders,start=1):
    queue.append((i,order))
while queue:
    num,move=queue.popleft()
    answer.append(num)
    if move>0:
        queue.rotate(-(move-1))
    else:
        queue.rotate(-move)
print(*answer)