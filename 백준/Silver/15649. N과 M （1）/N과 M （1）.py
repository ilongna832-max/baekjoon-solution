from itertools import permutations
a,b=map(int,input().split())
answer=[i for i in range(1,a+1)]
total=list(permutations(answer,b))
for i in total:
    print(*i)