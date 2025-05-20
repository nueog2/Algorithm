C = []

for _ in range(10):
    C.append(int(input())%42)

# print(C)
setC = set(C)
print(len(setC))