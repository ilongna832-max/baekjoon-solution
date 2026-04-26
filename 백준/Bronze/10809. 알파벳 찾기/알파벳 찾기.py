a=input()
answer=[-1]*26
for i in range(len(a)):
    count=ord(a[i])-ord('a')
    if answer[count]==-1:
        answer[count]=i
for i in answer:
    print(i,end=' ')