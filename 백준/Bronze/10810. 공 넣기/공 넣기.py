a,b=map(int,input().split())
baskets=[0]*(a+1)
for _ in range(b):
    num1,num2,num3=map(int,input().split())
    for j in range(num1,num2+1):
        baskets[j]=num3
for i in range(1,a+1):
    print(baskets[i],end=' ')