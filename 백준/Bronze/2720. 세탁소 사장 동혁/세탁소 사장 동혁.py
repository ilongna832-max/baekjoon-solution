a=int(input())
money=[25,10,5,1]
for _ in range(a):
    result=[]
    b=int(input())
    for i in money:
        total=b//i
        result.append(total)
        b=b%i
    print(' '.join(str(j) for j in result))