from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic={}
    for a,b in zip(want,number):
        dic[a]=b
    #날짜별로 개수 측정
    total=[]
    for i in range(len(discount)):
        items=discount[i:i+10]
        count=Counter(items)
         #날짜마다 개수 맞는지 확인
        if dic==count:
            answer+=1
        
    return answer