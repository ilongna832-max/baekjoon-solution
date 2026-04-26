from collections import deque
a=int(input())
queue=deque()
for _ in range(a):
    total,order=map(int,input().split())
    num=list(map(int,input().split()))
    queue=deque([(v,i) for i,v in enumerate(num)])
    count=0
    while queue:
        start=queue.popleft()
        if any(start[0]<j[0] for j in queue):
            queue.append(start)
        else:
            count+=1
            if start[1]==order:
                print(count)
                break