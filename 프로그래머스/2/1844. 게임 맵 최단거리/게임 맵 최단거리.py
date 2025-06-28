# BFS , 도달할 수 있는 최소 거리 

from collections import deque

def solution(maps):
    answer = -1
    
    queue = deque()
    m = len(maps)
    n = len(maps[0])
    
    visited = [[0]*n for _ in range(m)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
                
    answer = maps[m-1][n-1]
    if answer == 1:
        return -1
    return answer