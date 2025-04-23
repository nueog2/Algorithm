N = int(input())
size = list(map(int,input().split()))
T,P = map(int,input().split())
howmuch = 0
howmanypen = 0


for i in range(6):
    if size[i]%T == 0:
        howmuch += size[i]//T
    else: howmuch += (size[i]//T)+1

howmanypen = N//P
zaru = N%P

print(howmuch)
print(howmanypen,zaru)