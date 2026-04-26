a=input()
num1=0
num2=0
first=a[0]
if first=='0':
    num1=1
else:
    num2=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        if a[i+1]=='1':
            num2+=1
        else:
            num1+=1
print(min(num1,num2))