
import sys
sys.setrecursionlimit(10000)

N = int(input())
# M = [list(input().strip()) for _ in range(N)]
M = [list(map(int,input().strip())) for _ in range(N)]

def dfs(x,y):
    M[x][y] = -1 #방문 처리 
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    house = 1 #자신도 집 개수에 포함

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ( 0 <= nx < N) and (0 <= ny < N) and M[nx][ny] == 1:
            # M[nx][ny] = -1
            house += dfs(nx,ny)
                
    return house


단지수 = 0
houselist = []

for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            house = dfs(i,j)
            houselist.append(house)
            단지수 += 1

print(단지수)
# print(sorted(houselist))
for i in sorted(houselist):
    print(i)
