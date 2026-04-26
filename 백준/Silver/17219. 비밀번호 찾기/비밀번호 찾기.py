a,b=map(int,input().split())
dic={}
for _ in range(a):
    site,id=input().split()
    dic[site]=id
for _ in range(b):
    answer=input()
    print(dic[answer])