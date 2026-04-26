import math
import sys
input=sys.stdin.readline
max_range=1000000
answer=[True]*(max_range+1)
answer[0]=answer[1]=False
for i in range(2,int(max_range**0.5)+1):
    if answer[i]:
        for k in range(i*i,max_range+1,i):
            answer[k]=False
count=0
max_count=[]
a=int(input())
for _ in range(a):
    b=int(input())
    count=0
    for j in range(2,b//2+1):
        if answer[j] and answer[b-j]:
            count+=1
    max_count.append(count)
for k in max_count:
    print(k)
