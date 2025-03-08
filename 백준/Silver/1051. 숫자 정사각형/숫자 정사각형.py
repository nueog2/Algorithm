y,x = map(int,input().split())

A = [list(input().strip()) for _ in range(y)]

max_square =1

for i in range(y):
    for j in range(x):
        for z in range(1,min(y-i,x-j)):
            if A[i][j] == A[i+z][j] == A[i][j+z] == A[i+z][j+z]:
                max_square = max(max_square,(z+1)*(z+1))
                    
print(max_square)