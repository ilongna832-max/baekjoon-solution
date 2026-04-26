import math
a,b,c=list(map(int,input().split()))
count=c-a
gain=a-b
if a>=c:
    print(1)
else:
    answer=math.ceil(count/gain)+1
    print(answer)