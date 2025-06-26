N = int(input())
list = []

for _ in range(N):
    list.append(int(input()))

lists = sorted(list)

for i in range(len(lists)):
    print(lists[i])