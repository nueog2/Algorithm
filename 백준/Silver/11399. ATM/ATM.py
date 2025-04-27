N = int(input())
p = list(map(int,input().split()))

p.sort()
sum_time = 0
total = 0
 
for time in p:
    sum_time += time
    total += sum_time

print(total)
