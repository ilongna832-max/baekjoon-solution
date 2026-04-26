a,b = map(int, input().split())
c=int(input())
total=a*60+b+c
time=total//60
minute=total%60
final=time%24
print(final,minute)
