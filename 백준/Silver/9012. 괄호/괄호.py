
a=int(input())
answer=[]
for _ in range(a):
    stack=[]
    total=True
    b=input().strip()
    for i in b: 
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack:
                stack.pop()
            else:
                total=False
                break
    if total and not stack:
        answer.append('YES')
    else:
        answer.append('NO')
for i in answer:
    print(i)