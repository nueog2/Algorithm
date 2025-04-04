import sys

m = int(sys.stdin.readline())
total = 0
num = list(sys.stdin.readline().strip())
    
if len(num) == m:
    for i in num:
        total += int(i)
print(total)    