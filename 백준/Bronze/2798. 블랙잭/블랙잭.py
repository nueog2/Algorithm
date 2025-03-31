from itertools import combinations

N,M = map(int,input().split())
card = list(map(int,input().split()))
# diff = float('inf')
cardsum = 0

for cardlist in combinations(card,3):
    if sum(cardlist) <= M:
        # if abs(sum(cardlist)-M) < diff:
        cardsum = max(cardsum,sum(cardlist))             
print(cardsum)