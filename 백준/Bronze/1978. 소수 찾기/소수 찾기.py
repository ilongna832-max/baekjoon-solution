a=int(input())
b=list(map(int,input().split()))
count=0
def is_prime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
for j in b:
   if is_prime(j):
       count+=1
print(count)