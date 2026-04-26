a=input()
b=set()
c=len(a)
for i in range(c):
    for j in range(i+1,c+1):
        b.add(a[i:j])
print(len(b))