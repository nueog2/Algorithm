TC = int(input())
cup_location = 1

for _ in range(TC):
    a,b = map(int,input().split())
    if cup_location == a:
        cup_location = b
    elif cup_location == b:
        cup_location = a


print(cup_location)