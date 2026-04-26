a,b=map(int,input().split())
count=''
while a>0:
    remain=a%b
    a=a//b
    if remain<10:
        count+=str(remain)
    elif 10<=remain<36:
        count+=chr(remain+55)
count=count[::-1]
print(count)