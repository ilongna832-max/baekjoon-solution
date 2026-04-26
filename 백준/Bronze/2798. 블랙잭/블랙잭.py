from itertools import combinations
a,b=list(map(int,input().split()))
num=list(map(int,input().split()))
answer=0
for i in combinations(num,3):
  total=sum(i)
  if total>answer and total<=b:
    answer=total
print(answer)
