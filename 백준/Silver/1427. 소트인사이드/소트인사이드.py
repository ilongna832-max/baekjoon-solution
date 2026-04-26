a=str(input())
b=[]
for i in a:
    b.append(i)
answer=sorted(b,reverse=True)
total=''.join(answer)
print(int(total))