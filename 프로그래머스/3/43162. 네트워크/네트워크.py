def solution(n, computers):

    visited = [0] * (n)
    answer = 0

    # dfs 
    def dfs(c):
        visited[c] = 1

        for i in range(n):
            if i != c and computers[c][i] == 1:
                if visited[i] == 0:
                    dfs(i)

    # 컴퓨터 하나씩 start 지점으로 다 방문해야함
    for c in range(n):
        if visited[c] == 0:
            dfs(c)
            answer += 1
            
    return answer

