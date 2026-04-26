import statistics
import sys
input=sys.stdin.readline
a=int(input())
answer=[]
for _ in range(a):
    b=int(input())
    answer.append(b)
total=statistics.multimode(answer)
total.sort()
print(round(sum(answer)/a))
print((statistics.median(answer)))
if len(total)>1:
    print(total[1])
else:
    print(total[0])
print(max(answer)-min(answer))