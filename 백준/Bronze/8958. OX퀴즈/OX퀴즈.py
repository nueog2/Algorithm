n = int(input())

for i in range(n):
    t = list(input())
    cnt, res = 0, 0  #연속되는 O의 개수, 총 점수
    for j in t:
        if j == "O":
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)
