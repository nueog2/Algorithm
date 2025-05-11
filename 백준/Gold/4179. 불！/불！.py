import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(check):
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c:
        if maze[nx][ny] == '.'or maze[nx][ny] == 'J':
          if check == 'J':
            if dis_j[nx][ny] == -1:
              dis_j[nx][ny] = dis_j[x][y] + 1
              q.append((nx,ny))
          if check == 'F':
            if dis_f[nx][ny] == -1:
              dis_f[nx][ny] = dis_f[x][y] + 1
              q.append((nx,ny))
          

r, c = map(int, sys.stdin.readline().split())
maze = [list(map(str, list(sys.stdin.readline().strip()))) for _ in range(r)]
dis_j = [[-1 for _ in range(c)] for _ in range(r)]
dis_f = [[-1 for _ in range(c)] for _ in range(r)]
q = deque()
# J의 초기 위치 설정
for i in range(r):
  for j in range(c):
    if maze[i][j] == 'J':
      q.append((i,j))
      dis_j[i][j] = 0
bfs('J')
q = deque()
# F의 초기 위치 설정
for i in range(r):
  for j in range(c):
    if maze[i][j] == 'F':
      q.append((i,j))
      dis_f[i][j] = 0
bfs('F')

# 최단 시간 계산
min_time = float('inf')
for i in range(r):
    for j in range(c):
        if (i == 0 or i == r-1 or j == 0 or j == c-1) and dis_j[i][j] != -1:
            if dis_j[i][j] < dis_f[i][j] or dis_f[i][j] == -1:
                min_time = min(min_time, dis_j[i][j])
# 결과 출력                
if min_time == float('inf'):
    print("IMPOSSIBLE")
else:
    print(min_time + 1)