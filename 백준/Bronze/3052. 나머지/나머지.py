answer=[]
number=set()
for _ in range(10):
    a=int(input())
    answer.append(a)
for i in answer:
    b=i%42
    number.add(b)
print(len(number))