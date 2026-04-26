a = int(input())
time = list(map(int, input().split()))
time.sort()
total=0
waiting=0
for j in time:
    waiting+=j
    total+=waiting
print(total)