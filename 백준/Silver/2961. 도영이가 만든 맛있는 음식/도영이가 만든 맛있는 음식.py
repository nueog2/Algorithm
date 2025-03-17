from itertools import combinations

N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')  

for r in range(1,N+1):
    for sblist in combinations(ingredients,r):
        sour = 1
        bitter = 0
        for s,b in sblist:
            sour *= s
            bitter += b
        min_diff = min(min_diff, abs(sour-bitter))

print(min_diff)