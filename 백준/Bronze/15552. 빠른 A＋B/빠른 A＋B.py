import sys

# 1. sys.stdin.readline()을 사용하여 테스트 케이스의 개수 T를 입력받아 정수로 변환합니다.
# strip() 또는 rstrip()을 사용하여 개행 문자(\n)를 제거합니다.
T = int(sys.stdin.readline().strip())

# 2. T번 반복
for _ in range(T):
    # 3. sys.stdin.readline()으로 한 줄(A와 B)을 입력받아 빠르게 처리합니다.
    # .split()으로 공백을 기준으로 나눈 후, map(int, ...)로 정수로 변환합니다.
    A, B = map(int, sys.stdin.readline().split())
    
    # 4. A + B 결과를 출력합니다.
    # print()는 내부적으로 효율적으로 작동하므로, 별도의 sys.stdout.write는 생략하는 경우가 많습니다.
    print(A + B)