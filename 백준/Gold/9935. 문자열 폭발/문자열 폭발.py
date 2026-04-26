import sys
input=sys.stdin.readline
a=input().strip()
b=input().strip()
stack=[]
for i in a:
    stack.append(i)
    total=len(b)
    if len(stack)>=total:
        if ''.join(stack[-total:])==b:
            del stack[-total:]
if not stack:
    print('FRULA')
else:
    print(''.join(map(str,stack)))