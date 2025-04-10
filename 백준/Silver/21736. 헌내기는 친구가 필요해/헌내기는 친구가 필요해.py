import sys
sys.setrecursionlimit(1000000)

N,M = map(int,sys.stdin.readline().split())

campus = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def dfs(x,y):
    global meet 
    visited[x][y] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ( 0 <= nx < N) and ( 0 <= ny < M) :
            if visited[nx][ny] == 0 and campus[nx][ny] != "X":
                if campus[nx][ny] == "P":
                    meet += 1
                dfs(nx, ny)
    return meet

meet = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            meet = dfs(i,j)

print("TT" if meet == 0 else meet)
