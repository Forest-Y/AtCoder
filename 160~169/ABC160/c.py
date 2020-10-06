
k, n = map(int, input().split())
a = list(map(int, input().split()))

dist = [0] * n
dist[0] = k - a[n - 1] + a[0]
for i in range(1, n):
    dist[i] = a[i] - a[i - 1]

print(k - max(dist))