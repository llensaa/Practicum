n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for m in range(n + 1):
    for k in range(1, n + 1):
        if m == 0:
            dp[m][k] = 1
        else:
            if k > m:
                dp[m][k] = dp[m][m]
            else:
                dp[m][k] = dp[m - k][k - 1] + dp[m][k - 1]
result = dp[n][n]
print(result)