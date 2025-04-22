from collections import deque

N,K = map(int,input().split())
visited = [0]*100001


def bfs():
    queue = deque()
    queue.append(N)
    
    while queue:
        a = queue.popleft()    
        if a == K:
            print(visited[K])
            continue

        for i in (a-1,a+1,a*2):
            if 0<= i <= 100000 and not visited[i]:
                visited[i] = visited[a]+1
                queue.append(i)

bfs()