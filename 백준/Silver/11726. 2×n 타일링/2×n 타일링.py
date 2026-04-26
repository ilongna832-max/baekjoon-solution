import sys
input=sys.stdin.readline
a=int(input())
if a==1:
    print(1)
elif a==2:
    print(2)
else:
    dp=[0]*(a+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,a+1):
        dp[i]=(dp[i-1]+dp[i-2])%10007
    print(dp[a])