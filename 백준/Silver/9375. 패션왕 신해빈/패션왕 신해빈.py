import sys
input=sys.stdin.readline
a=int(input())
for _ in range(a):
    count=1
    b=int(input())
    dic={}
    for _ in range(b):
        cloth,kind=input().split()
        if kind not in dic:
            dic[kind]=1
        else:
            dic[kind]+=1
    for i in dic.values():
        count*=i+1
    print(count-1)