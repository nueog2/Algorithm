n = int(input())
nums = list(map(int, input().split()))
count = 0

for x in nums:
    if x < 2:
        continue  
    is_prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime == True:
    # if is_prime: 으로 적어도 됨.     
        count += 1

print(count)
# 참고, 1 하고 0은 소수가 아님. 