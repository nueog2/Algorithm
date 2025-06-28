
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    unique_nums = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))  # '0','1','1' → '011' → 11
            unique_nums.add(num)
    
    ans = 0
    for num in unique_nums:
        if is_prime(num):
            ans += 1
    
    return ans

