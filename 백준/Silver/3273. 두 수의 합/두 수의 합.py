n = int(input())
b = list(map(int, input().split()))
b.sort()
target = int(input())

start = 0
end = n - 1
count = 0

while start < end:
    total = b[start] + b[end]
    if total == target:
        count += 1
        start += 1
        end -= 1
    elif total < target:
        start += 1
    else:
        end -= 1
print(count)