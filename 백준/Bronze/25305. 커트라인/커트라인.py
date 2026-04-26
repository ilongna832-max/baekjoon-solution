m,n= map(int, input().split())
b = list(map(int, input().split()))
b.sort(reverse=True)
print(b[n-1])