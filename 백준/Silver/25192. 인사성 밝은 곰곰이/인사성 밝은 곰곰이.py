import sys
input=sys.stdin.readline
a=int(input())
b=set()
count=0
for _ in range(a):
    chat=input().strip()
    if chat=='ENTER':
        b=set()
    else:
        if chat not in b:
            b.add(chat)
            count+=1
print(count)