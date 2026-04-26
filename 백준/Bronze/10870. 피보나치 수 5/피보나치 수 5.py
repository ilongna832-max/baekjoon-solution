a=int(input())
def num(b):
    if b==0:
        return 0
    elif b==1:
        return 1
    elif b>=2:  
        return num(b-1)+num(b-2)
print(num(a))