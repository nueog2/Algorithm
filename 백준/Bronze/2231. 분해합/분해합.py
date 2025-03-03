N = int(input())

for x in range(1, N+1):
    num_sum = x + sum(map(int, str(x))) # x의 각 자릿수를 더한 후 
    # 분해합 = 생성자 + 각 자릿수의 합 
    if num_sum == N:
        print(x)
        break
else:
    print(0)