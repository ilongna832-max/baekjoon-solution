import math 
import sys
input=sys.stdin.readline
a=int(input())
for _ in range(a):
    b,c=map(int,input().split())
    answer=math.lcm(b,c)
    print(answer)