
a=int(input())

b=int(input())

answer=[]

def is_prime(num):

    if num==1:

        return False

    else:

        for i in range(2,int(num**0.5)+1):

            if num%i==0:

              return False

        return True

for j in range(a,b+1):

    if is_prime(j)==True:

        answer.append(j)
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)