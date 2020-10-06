
n, k = map(int, input().split())
p = list(map(int, input().split()))
ans = 0
for i in range(k):
    ans += (p[i] + 1) / 2
calc = ans
for i in range(1, n - k + 1):
    calc += ((p[i + k - 1] + 1) - (p[i - 1] + 1)) / 2
    ans = max(ans, calc)
print(ans)