from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
answer=[]
que=deque()
for _ in range(a):
    line=input().split()
    k=line[0]
    if k=='1':
        que.appendleft(int(line[1]))
    elif k=='2': 
        que.append(int(line[1]))
    elif k=='3':
        answer.append(que.popleft() if que else -1)
    elif k=='4': 
        answer.append(que.pop() if que else -1)
    elif k=='5':
        answer.append(len(que))
    elif k=='6':
        answer.append(1 if not que else 0)
    elif k=='7':
        answer.append(que[0] if que else -1)
    elif k=='8': 
        answer.append(que[-1] if que else -1)
print(*answer,sep='\n')
        
        
    


        


                
                    

