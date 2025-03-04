import random 

N = 9
L = []

for i in range(N):
    L.append(int(input()))


while True : 
    sampleL = random.sample(L,7)
    if sum(sampleL) == 100:
        sampleL.sort()
        for i in sampleL:
            print(i)
        break
