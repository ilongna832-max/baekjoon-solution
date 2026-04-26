import sys
input=sys.stdin.readline
a=int(input())
stack=[]
answer=[]
start=1
current=True
for _ in range(a):
    b=int(input())
    while start<=b:
        stack.append(start)
        answer.append('+')
        start+=1
    if not stack or stack[-1]!=b:
        current=False
        break
    else:
        stack.pop()
        answer.append('-')
if current:
    print('\n'.join(answer))
else:
    print('NO')