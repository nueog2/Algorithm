from itertools import combinations

N,M = map(int,input().split())
card = list(map(int,input().split()))
cardsum = 0

for cardlist in combinations(card,3):
    if sum(cardlist) <= M:
        cardsum = max(cardsum,sum(cardlist))             
print(cardsum)