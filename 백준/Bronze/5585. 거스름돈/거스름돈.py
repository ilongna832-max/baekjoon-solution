a=int(input())
b=[500,100,50,10,5,1]
total=1000-a
count=0
for i in b:
    remain=total//i
    count+=remain
    total=total%i
    if total==0:
        break
print(count)