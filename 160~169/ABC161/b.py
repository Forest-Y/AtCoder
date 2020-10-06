
n, m = map(int, input().split())
a = list(map(int, input().split()))

mean = sum(a) / m / 4
cnt = 0
for i in range(n):
    if a[i] >= mean:
        cnt += 1

print("Yes" if cnt >= m else "No")