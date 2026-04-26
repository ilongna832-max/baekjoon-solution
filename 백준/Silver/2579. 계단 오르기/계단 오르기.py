a=int(input())
b=[0]*301
for i in range(1,a+1):
    b[i]=int(input())
if a==1:
    print(b[1])
elif a==2:
    print(b[1]+b[2])  
else:
    dp=[0]*301
    dp[1]=b[1]
    dp[2]=b[1]+b[2]
    dp[3]=max(b[1]+b[3],b[2]+b[3])
    for i in range(4,a+1):
        dp[i]=max(dp[i-3]+b[i-1]+b[i],dp[i-2]+b[i])
    print(dp[a])