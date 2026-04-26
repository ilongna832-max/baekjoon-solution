import sys
input=sys.stdin.readline
while True:
    stack=[]
    a=input().rstrip('\n')
    answer=True
    if a=='.':
        break
    for i in a:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if not stack or stack[-1]!='(':
                answer=False
                break
            stack.pop()
        elif i==']':
            if not stack or stack[-1]!='[':
                answer=False
                break
            stack.pop()
    if not stack and answer:
        print('yes')
    else:
        print('no')