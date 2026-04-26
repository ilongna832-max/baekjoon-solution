a=int(input())
total=1
for i in range(1,a+1):
    total*=i
total=str(total)[::-1]
count=0
for j in range(len(total)):
    if total[j]=='0':
        count+=1
    else:
        break
print(count)