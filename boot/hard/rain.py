n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
x = 0
for i in range(1, n, 2):
    x += a[i]

ans[0] = sum(a) - 2 * x
for i in range(1, n):
    ans[i] = 2 * a[i - 1] - ans[i - 1]

print(*ans)