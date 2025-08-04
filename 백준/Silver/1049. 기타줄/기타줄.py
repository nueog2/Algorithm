N,M = map(int,input().split())

p = []
s = []

for _ in range(M):
    a,b = map(int,input().split())
    p.append(a)
    s.append(b)

money,money2,money3 = 0,0,0

money += (min(s)*(N%6))+(min(p)*(N//6))

money2 += min(p)*((N//6)+1)

money3 += min(s)*N

print(min(money,money2,money3))