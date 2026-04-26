import sys
input=sys.stdin.readline
a=int(input())
answer=set()
color='ChongChong'
for _ in range(a):
    b,c=map(str,input().split())
    if b==color or c==color:
        answer.add(b)
        answer.add(c)
    if b in answer or c in answer:
        answer.add(c)
        answer.add(b)
print(len(answer))
        
