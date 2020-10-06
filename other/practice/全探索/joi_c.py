
n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort()
exist = set(data)
ans = 0
for i in range(n):
    x1, y1 = data[i]
    for j in range(i + 1, n):
        x2, y2 = data[j]
        dx = x2 - x1
        dy = y2 - y1
        if (x1 - dy, y1 + dx) in exist and (x2 - dy, y2 + dx) in exist:
            ans = max(ans, dx ** 2 + dy ** 2)

print(ans)