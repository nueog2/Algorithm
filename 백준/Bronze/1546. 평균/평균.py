N = int(input())
scores = list(map(int,input().split()))
maxscore = 0

for i in range(N) :
    if maxscore < scores[i] :
        maxscore = scores[i]

for i in range(N):
    scores[i] = scores[i]/maxscore*100

print(sum(scores)/N)