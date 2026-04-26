
answer=int(input())

for i in range(answer):

    a,b=map(int,input().split())

    c=a+b

    print(f"Case #{i+1}: {a} + {b} = {c}")