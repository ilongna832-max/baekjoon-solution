import sys
input=sys.stdin.readline
a=int(input())
answer=set()
for _ in range(a):
    order=input().split()
    b=order[0]
    if b=='all':
        answer=set(range(1,21))
    elif b=='empty':
        answer=set()
    else: 
        c=int(order[1])
        if b=='add':
            answer.add(c)
        elif b=='remove':
            answer.discard(c)
        elif b=='check':
            print(1 if c in answer else 0)
        elif b=='toggle':
            if c in answer:
                answer.remove(c)
            else:
                answer.add(c)
        