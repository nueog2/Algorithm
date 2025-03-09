
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    cycle = [a % 10]  

    while True:  
        next_digit = (cycle[-1] * (a % 10)) % 10
        if next_digit == cycle[0]:  
            break
        cycle.append(next_digit)

    print(cycle[(b - 1) % len(cycle)] or 10)