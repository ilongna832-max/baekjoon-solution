a=[input() for _ in range(3)]
count=0
for i in range(3):
    if a[i].isdigit():
        count=int(a[i])+(3-i)
if count%3==0 and count%5==0:
    print('FizzBuzz')
elif count%3==0:
    print('Fizz')
elif count%5==0:
    print('Buzz')
else:
    print(count)