a=int(input())
group=1
while group<a:
    a-=group
    group+=1
if group%2==0:
    up=a
    down=group-a+1
else:
    up=group-a+1
    down=a
print(f"{up}/{down}")