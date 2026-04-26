a,b=map(int,input().split())
kind=[]
count=0
for _ in range(a):
    coin=int(input())
    kind.append(coin)
kind.sort(reverse=True)
for i in kind:
    if b==0:
        break
    max_count=b//i
    count+=max_count
    b=b%i
print(count)
    