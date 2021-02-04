n, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (w + 1) for i in range(n)]
for i in range(n):
    for j in range(w + 1):
        if j - data[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - data[i][0]] + data[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[-1]))
