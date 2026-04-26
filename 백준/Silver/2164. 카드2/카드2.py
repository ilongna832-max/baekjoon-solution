from collections import deque
a=int(input())
b=deque()
for i in range(1,a+1):
    b.append(i)
while len(b)>1:
    b.popleft()
    b.rotate(-1)
print(b[0])
