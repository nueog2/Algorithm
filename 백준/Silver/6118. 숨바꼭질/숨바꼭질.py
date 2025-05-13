import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
way = [0]*(N+1)


queue.append(1)

while queue:
    x = queue.popleft()
    visited[x] = 1
    for next in graph[x]:
        if visited[next] == 0:
            visited[next] = 1
            way[next] = way[x] + 1
            queue.append(next)

maxway = max(way)
hlist = []
for i in range(len(way)):
    if maxway == way[i]:
        hlist.append(i)
hlist.sort()

print(hlist[0],maxway,len(hlist))