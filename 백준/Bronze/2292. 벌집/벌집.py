a=int(input())
max=1
layer=1
add=6
while a>max:
    max+=add
    add+=6
    layer+=1
print(layer)
