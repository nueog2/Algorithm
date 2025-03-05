TC = int(input())
k = [int(input()) for _ in range(TC)]  

def eureka(num):
    T = [i * (i + 1) // 2 for i in range(1, 45)]  
    for x in range(len(T)):
        for y in range(len(T)):
            for z in range(len(T)):
                if T[x] + T[y] + T[z] == num:
                    return 1  
    return 0  

for num in k:
    print(eureka(num))  