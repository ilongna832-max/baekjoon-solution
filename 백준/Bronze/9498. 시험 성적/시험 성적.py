a = int(input()) # 자료형 변환 (1번 문제 해결)

if a >= 90: # 90점 이상
    print('A')
elif a >= 80: # 80점 이상 90점 미만
    print('B')
elif a >= 70: # 70점 이상 80점 미만
    print('C')
elif a >= 60: # 60점 이상 70점 미만
    print('D')
else: # 60점 미만
    print('F')
