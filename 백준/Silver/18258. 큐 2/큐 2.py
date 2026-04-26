from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
queue=deque()
answer=[]
for _ in range(a):
    line=input().split()
    b=line[0]
    if b=='push':
        queue.append(line[1])
    elif b=='pop':
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif b=='size':
        answer.append(len(queue))
    elif b=='empty':
        if not queue:
            answer.append(1)
        else:
            answer.append(0)
    elif b=='front':
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif b=='back':
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)
print(*answer,sep='\n')



        


                
                    

