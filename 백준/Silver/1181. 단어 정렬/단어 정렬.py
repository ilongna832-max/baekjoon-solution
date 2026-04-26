a=int(input())
b=set()
for _ in range(a):
    c=input()
    b.add(c)
answer=sorted(b,key=lambda x:(len(x),x))
for i in answer:
    print(i)