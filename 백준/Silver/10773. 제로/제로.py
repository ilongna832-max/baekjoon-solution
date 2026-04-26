a=int(input())
answer=[]
for _ in range(a):
    b=int(input())
    if b!=0:
        answer.append(b)
    else:
        answer.pop()
print(sum(answer))
