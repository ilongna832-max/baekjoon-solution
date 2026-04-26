import sys
input=sys.stdin.readline
a=int(input())
start=666
count=0
while True:
    if '666' in str(start):
        count+=1
    if a==count:
        break
    start+=1
print(start)