n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * n
dp[1] = abs(h[0] - h[1])

for i in range(2, n):
    score = 10 ** 20
    for j in range(1, min(k, i) + 1):
        score = min(score, dp[i - j] + abs(h[i - j] - h[i]))
    dp[i] = score
print(dp[-1])