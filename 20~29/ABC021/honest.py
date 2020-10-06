n = int(input())
a, b = map(int, input().split())
m = int(input())
x, y = [0] * m, [0] * m
data = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    data[x - 1].append(y - 1)
    data[y - 1].append(x - 1)

dist = [[-1] * n for i in range(n)]
dist[a - 1][b - 1] = 0