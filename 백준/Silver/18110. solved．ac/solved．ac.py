import sys
input=sys.stdin.readline
a=int(input())
b=[int(input()) for _ in range(a)]
b.sort()
if a==0:
    print(0)
else: 
    order=int(len(b)*0.15+0.5)
    answer=b[order:len(b)-order]
    print(int(sum(answer)/len(answer)+0.5))