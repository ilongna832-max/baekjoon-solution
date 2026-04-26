a=int(input())
answer=[int(input()) for _ in range(a)]
answer.sort()
weight=0
for i in range(a):
    current=answer[i]*(a-i)
    if current>weight:
        weight=current
print(weight)