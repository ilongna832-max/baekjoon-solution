a=int(input())
b=list(map(int,input().split()))
dp=[0]*a
dp[0]=b[0]
for i in range(1,len(b)):
    dp[i]=max(b[i],dp[i-1]+b[i])
print(max(dp))