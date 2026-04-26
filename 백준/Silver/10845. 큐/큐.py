from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
answer=deque()
for _ in range(a):
    b=input().split()
    if b[0]=='push':
        answer.append(b[1])
    elif b[0]=='pop':
        if answer:
            print(answer.popleft())
        else:
            print(-1)
    elif b[0]=='size':
        print(len(answer))
    elif b[0]=='empty':
        if not answer:
            print(1)
        else:
            print(0)
    elif b[0]=='front':
        if answer:
            print(answer[0])
        else:
            print(-1)
    elif b[0]=='back':
        if answer:
            print(answer[-1])
        else:
            print(-1)
