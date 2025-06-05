from collections import deque
queue = deque()

N,M = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(0,N):
    for j in range(0,M):
        if space[i][j] == 1:
            queue.append((i,j))

while queue:
    x,y = queue.popleft()
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
        nx,ny = x+dx,y+dy

        if 0 <= nx < N and 0 <= ny < M:
            if space[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

maxfar = 0

for i in range(0,N):
    for j in range(0,M):
        if space[i][j] == 0 and visited[i][j] != 0:
            maxfar = max(maxfar,visited[i][j])
print(maxfar)