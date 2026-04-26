
a,b=map(int,input().split())
c={input() for _ in range(a)}
d={input() for _ in range(b)}
answer=list(c&d)
answer.sort()
print(len(answer))
print('\n'.join(answer))