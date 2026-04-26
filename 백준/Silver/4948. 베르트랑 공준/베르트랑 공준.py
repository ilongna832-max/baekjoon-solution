import math
import sys
max_range=123456*2
answer=[True]*(max_range+1)
answer[0]=answer[1]=False
for i in range(2,int(math.sqrt(max_range))+1):
    if answer[i]:
        for j in range(i*i,max_range+1,i):
            answer[j]=False
total=[]
sys=sys.stdin.readline
while True:
    a=int(input())
    if a==0:
        break
    count=answer[a+1:2*a+1].count(True)
    total.append(count)
print(*total,sep='\n')

    
        

        


    

                    
        
        

