import math
import sys
input=sys.stdin.readline
a=int(input())
length=[]
answer=[]
for _ in range(a):
    b=int(input())
    length.append(b)
length.sort()
for i in range(len(length)-1):
    row=length[i+1]-length[i]
    answer.append(row)
standard=answer[0]
for j in range(1,len(answer)):
    standard=math.gcd(standard,answer[j])
total_length=length[-1]-length[0]
total_count=(total_length//standard)+1
count=total_count-len(length)
print(count)


    
        