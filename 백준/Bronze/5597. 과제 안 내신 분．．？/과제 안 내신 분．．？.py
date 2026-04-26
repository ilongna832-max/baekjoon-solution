answer=[]
total=[]
for _ in range(28):
    a=int(input())
    answer.append(a)
for i in range(1,31):
    if i not in answer:
        total.append(i)
a=sorted(total)
print(min(a))
print(max(a))
        
        