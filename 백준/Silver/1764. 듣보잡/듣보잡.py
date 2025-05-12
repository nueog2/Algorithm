N, M = map(int, input().split())
l = set()  # 듣
s = set()  # 보

for _ in range(N):
    l.add(input())

for _ in range(M):
    s.add(input())

ls = sorted(list(l & s))

print(len(ls))
for i in ls:
    print(i)