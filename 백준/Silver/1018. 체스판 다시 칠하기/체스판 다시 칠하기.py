
y, x = map(int, input().split())  
A = [list(input().strip()) for _ in range(y)]  

min_repaint = float('inf')  

for i in range(y - 7):
    for j in range(x - 7):
        wrong_w = 0
        wrong_b = 0

        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    if A[i + row][j + col] != 'W':  
                        wrong_w += 1
                    if A[i + row][j + col] != 'B':  
                        wrong_b += 1
                else:
                    if A[i + row][j + col] != 'B':  
                        wrong_w += 1
                    if A[i + row][j + col] != 'W':  
                        wrong_b += 1

        min_repaint = min(min_repaint, min(wrong_w, wrong_b))  # 최소값 갱신

print(min_repaint)