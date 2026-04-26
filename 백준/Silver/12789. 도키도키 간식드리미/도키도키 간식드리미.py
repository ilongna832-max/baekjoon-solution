a=int(input())
order=list(map(int,input().split()))
stack=[]
target=1
for i in order:
    stack.append(i)
    while stack and stack[-1]==target:
        target+=1
        stack.pop()
if not stack:
    print('Nice')
else:
    print('Sad')
    