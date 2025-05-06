n = int(input())
nums = list(map(int, input().split()))
count = 0

for x in nums:
    if x == 1:
        continue

    for i in range(2,x):
        if x % i == 0:
            break
    else:
        count += 1

print(count)
