a=int(input())
for _ in range(a):
    b=int(input())
    max=100
    dp=[0]*(max+1)
    if b<=2:
        print(1)
    else:
        dp[1]=1
        dp[2]=1
        dp[3]=1
        for i in range(4,b+1):
            dp[i]=dp[i-2]+dp[i-3]
        print(dp[b])