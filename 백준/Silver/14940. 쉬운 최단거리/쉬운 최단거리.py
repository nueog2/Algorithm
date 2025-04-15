from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(map,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0 

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and map[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y]+1; 
                    queue.append((nx, ny))
            

n,m = map(int,input().split())
map = [list(map(int,input().split()))  for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            start = (i,j)
        elif map[i][j] == 0:
            visited[i][j] = 0

bfs(map,visited,start)

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=' ')
    print('')
            
