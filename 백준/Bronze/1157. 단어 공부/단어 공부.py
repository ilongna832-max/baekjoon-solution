a=input()
b=a.lower()
answer={}
for i in b:
    if i in answer:
        answer[i]+=1
    else:
        answer[i]=1
total=[]
c=max(answer.values())
for i,v in answer.items():
    if c==v:
        total.append(i)
if len(total)>=2:
    print('?')
else:
    print(total[0].upper())
        