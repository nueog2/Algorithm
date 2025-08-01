def solution(n, computers):
    
    visited = [0]*n
    answer = 0
    
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if i!=j and visited[j] == 0 and computers[i][j] == 1:
                dfs(j)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    
    return answer

