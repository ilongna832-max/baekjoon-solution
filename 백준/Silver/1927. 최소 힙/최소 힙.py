import heapq
import sys
input=sys.stdin.readline
a=int(input())
answer=[]
for _ in range(a):
    b=int(input())
    if b>0:
        heapq.heappush(answer,b)
    else:
        if not answer:
            print(0)
        else:
            print(heapq.heappop(answer))
