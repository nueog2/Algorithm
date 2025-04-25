from collections import deque

M, N, H = map(int, input().split())  
box = [[[0] * M for _ in range(N)] for _ in range(H)]  
queue = deque()

for h in range(H):
    for n in range(N):
        row = list(map(int, input().split()))
        for m in range(M):
            box[h][n][m] = row[m]
            if row[m] == 1:
                queue.append((h, n, m))  # z, y, x

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:  
                print(-1)
                exit(0)
            days = max(days, box[h][n][m])

print(days - 1)