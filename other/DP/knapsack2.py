n, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[float("inf")] * (10 ** 5 + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(10 ** 5 + 1):
        if j - data[i - 1][1] >= 0:
            dp[i][j] = min(dp[i - 1][j - data[i - 1][1]] + data[i - 1][0], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

for i in range(10 ** 5, 0, -1):
    if dp[-1][i] <= w:
        print(i)
        exit()