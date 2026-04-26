a=int(input())
for _ in range(a):
    count=0
    b=input()
    total=0
    for i in b:
        if i=='O':
            count+=1
            total+=count
        else:
            count=0
    print(total)
