n = int(input())
x, y = [0] * n, [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        d = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        ans = max(ans, d)

print(ans ** 0.5)
