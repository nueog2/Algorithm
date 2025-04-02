T = int(input())

for i in range(1,T+1):
    k = int(input())
    n = int(input())
    
    house = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(0,n+1):
        house[0][i] = i
    
    for x in range(1,k+1):
        for y in range(1,n+1):
            if y == 1:
                house[x][y] = house[x-1][y]
            house[x][y] = house[x][y-1]+house[x-1][y]
    print(house[k][n])