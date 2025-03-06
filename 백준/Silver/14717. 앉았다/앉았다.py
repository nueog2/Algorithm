
from itertools import combinations

a, b = map(int, input().split())

O = [1,2,3,4,5,6,7,8,9,10] * 2
O.remove(a)
O.remove(b)

p = 0  
total_cases = 0  

for c, d in combinations(O, 2):  
    total_cases += 1  
    
   
    if a == b:  
        if c == d:  
            if a > c:  
                p += 1
        else:
            p += 1  
    else:  
        if c == d:  
            continue
        if (a + b) % 10 > (c + d) % 10:
            p += 1


print(f"{p / total_cases:.3f}")
