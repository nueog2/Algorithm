import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    global count

    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)
    return count


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1 + N)
count = 0  #감염 컴퓨터 수 

bfs(1)
print(count)