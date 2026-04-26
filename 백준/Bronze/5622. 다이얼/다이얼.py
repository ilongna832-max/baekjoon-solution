a=input()
time=0
b=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in a:
    for j,k in enumerate(b):
        if i in k:
            time+=j+3
print(time)
