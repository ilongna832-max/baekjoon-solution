a=int(input())
for _ in range(a):
    b,c=map(str,input().split())
    for i in c:
        print(int(b)*i,end='')
    print()
