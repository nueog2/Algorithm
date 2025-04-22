
N = int(input())
dp = [5001]*(N+1)
dp[0] = 0


for i in range(1, N + 1):
    if i >= 3 and dp[i - 3] != 5001:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if i >= 5 and dp[i - 5] != 5001:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[N] == 5001:
    print(-1)
else: print(dp[N])
