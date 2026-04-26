while True:
    a=int(input())
    if a==-1:
        break
    answer=[]
    count=0
    for i in range(1,a):
        if a%i==0:
            answer.append(i)
            count+=i
    if count==a:
        total=' + '.join([str(j) for j in answer])
        print(f"{a} = {total}")
    else:
        print(f"{a} is NOT perfect.")