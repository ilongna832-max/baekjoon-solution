import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
answer=min(b)*max(b)
print(answer)
