n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = max(data[0][1], data[0][2])
dp[0][1] = max(data[0][0], data[0][2])
dp[0][2] = max(data[0][0], data[0][1])
for i in range(1, n):
    dp[i][0] = data[i][0] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = data[i][1] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = data[i][2] + max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[-1]))