a=int(input())
b=input()
count=0
num=31
remain=1234567891
for i in range(a):
    result=b[i]
    order=(ord(result)-ord('a')+1)
    total=(num**i)%remain
    count=(count+(order*total))%remain
print(count)