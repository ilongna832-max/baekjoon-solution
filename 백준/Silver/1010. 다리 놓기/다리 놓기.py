import math
import sys
input=sys.stdin.readline
a=int(input())
for _ in range(a):
    b,c=map(int,input().split())
    count=math.comb(c,b)
    print(count)
    