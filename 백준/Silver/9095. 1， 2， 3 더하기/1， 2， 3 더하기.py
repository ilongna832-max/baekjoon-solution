max=11
dp=[0]*(max+1)
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3,max+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
a=int(input())
for _ in range(a):
    total=int(input())
    print(dp[total])