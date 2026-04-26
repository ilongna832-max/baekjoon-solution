import heapq
import sys
input=sys.stdin.readline
answer=[]
a=int(input())
for _ in range(a):
    b=int(input())
    if b!=0:
        heapq.heappush(answer,(abs(b),b))
    else:
        if not answer:
            print(0)
        else:
            print(heapq.heappop(answer)[1])