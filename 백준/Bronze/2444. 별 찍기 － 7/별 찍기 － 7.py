a=int(input())
for i in range(1,a+1):
    space=a-i
    star=2*i-1
    print(' '*space+'*'*star)
for j in range(1,a):
    space=j
    star=2*(a-j)-1
    print(' '*space+'*'*star)