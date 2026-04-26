a=int(input())
count=0
for _ in range(a):
    b=input()
    answer=set()
    word=True
    for i in range(len(b)):
        if i==0 or b[i]==b[i-1]:
            answer.add(b[i])
        else:
            if b[i] in answer:
                word=False
                break
            else:
                answer.add(b[i])
    if word:
        count+=1  
print(count)