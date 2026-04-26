import math
def num(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
a=int(input())
answer=[]
for _ in range(a):
    n = int(input())
    while True:
        if num(n):
            answer.append(n)
            break
        n += 1     
for k in answer:
    print(k)
