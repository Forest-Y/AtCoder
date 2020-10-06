n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

ans = 0
for i in range(n - 1, -1, -1):
    ans += (b[i] - (a[i] + ans) % b[i]) % b[i]

print(ans)