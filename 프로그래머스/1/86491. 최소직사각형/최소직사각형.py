def solution(sizes):
    maxw = 0
    maxh = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1],sizes[i][0]
    
    for w, h in sizes:
        if w > maxw:
            maxw = w
        if h > maxh:
            maxh = h
    
    # for i in range(len(sizes)):
    #     if sizes[i][0] >= maxw:
    #         maxw = sizes[i][0]
    #     if sizes[i][1] >= maxh:
    #         maxh = sizes[i][1]

    
    return maxh*maxw

# 주어진 명함들의 가로 / 세로 길이를 비교한 후, 가로> 세로 일 경우 그대로 둔다. 
# 비교했을 때 가로 < 세로 일 경우 가로, 세로 길이를 바꿔준다. 
# 가로 / 세로 길이별 max 길이를 구한 후 지갑 크기를 구한다. 

