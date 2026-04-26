from collections import deque
a,b=map(int,input().split())
queue=deque(i for i in range(1,a+1))
answer=[]
for _ in range(a):
    queue.rotate(-(b-1))
    answer.append(queue.popleft())
print('<'+', '.join(map(str,answer))+'>')