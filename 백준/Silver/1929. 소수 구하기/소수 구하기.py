import math
def num(c):
    if c<2:
        return False
    for i in range(2,int(math.sqrt(c))+1):
        if c%i==0:
            return False
    return True
answer=[]
a,b=map(int,input().split())
for j in range(a,b+1):
    if num(j):
        answer.append(j)
print(*answer,sep='\n')
        