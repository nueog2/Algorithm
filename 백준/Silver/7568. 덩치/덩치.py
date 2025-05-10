N = int(input())
p = []
k = [1]*N

for _ in range(0,N):
    p.append(list(map(int,input().split())))


for i in range(0,N):
    for j in range(0,N):
        if i == j :
            continue
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            k[i] += 1

print(*k)