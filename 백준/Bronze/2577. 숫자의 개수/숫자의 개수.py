A = int(input())
B = int(input())
C = int(input())
howmany = [0]*10
num = str(A*B*C)

for i in range(len(num)):
    for j in range(0,10):
        if int(num[i]) == j:
            howmany[j] += 1

for i in range(len(howmany)):
    print(howmany[i])