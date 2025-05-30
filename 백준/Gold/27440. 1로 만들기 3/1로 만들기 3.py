from collections import deque

N = int(input())

def bfs(n):
    global cnt

    queue = deque()
    queue.append((n,0))
    visited = set()
    
    while queue:
        x,cnt = queue.popleft()

        if x == 1:
            return cnt
        if x%3 == 0 and x//3 not in visited:
            visited.add(x//3)
            queue.append((x//3,cnt+1))
        if x%2 == 0 and x//2 not in visited:
            visited.add(x//2)
            queue.append((x//2,cnt+1))
        if x-1 >= 1 and x-1 not in visited:
            visited.add(x-1)
            queue.append((x-1,cnt+1))

bfs(N)
print(cnt)