import sys
input=sys.stdin.readline
stack=[]
answer=[]
a=int(input())
for _ in range(a):
    line=input().split()
    order=line[0]
    if order=='1':
        stack.append(int(line[1]))
    elif order=='2':
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif order=='3':
        answer.append(len(stack))
    elif order=='4':
        answer.append(1 if not stack else 0)
    elif order=='5':
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
print(*answer,sep='\n')

            

        


                
                    

