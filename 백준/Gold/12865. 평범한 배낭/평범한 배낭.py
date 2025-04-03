
def bag(idx,weight):
    global memo

    if idx == N:
        return 0
    
    if (idx,weight) in memo:
        return memo[(idx,weight)]

    res = bag(idx+1,weight)

    if weight + items[idx][0] <= K:
        res = max(res,items[idx][1] + bag(idx+1,weight + items[idx][0]))
    
    memo[(idx,weight)] = res
    return res
    

N,K = map(int,input().split())
items = [() for _ in range(N)]

for i in range(N):
    a,b = map(int,input().split())
    items[i] = (a,b)

answer = 0
memo = {}

print(bag(0,0))