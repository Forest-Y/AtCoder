n, x, y = map(int, input().split())

ans = [0] * (n - 1)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ans[min(abs(j - i), abs(x - i) + 1 + abs(y - j), abs(x - j) + 1 + abs(y - i)) - 1] += 1

for x in ans:
    print(x)