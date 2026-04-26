import sys
input=sys.stdin.readline
answer=[]
for _ in range(5):
    code=input().strip()
    answer.append(list(code))
#세로가 15개 까지 가능하니 세로 기준
for j in range(15):
    for i in range(5):
        #len으로 가로개수제한없앰
        if j<len(answer[i]):
            print(answer[i][j],end='')