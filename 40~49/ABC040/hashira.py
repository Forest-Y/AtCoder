n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 20
dp = [0] * n
def DP(dp):
    for i in range(1, n):
        if i == 1:
            dp[i] = abs(a[0] - a[1])
        else:
            dp[i] = min(dp[i - 2] + abs(a[i - 2] - a[i]), dp[i - 1] + abs(a[i - 1] - a[i]))

DP(dp)
print(dp[-1])