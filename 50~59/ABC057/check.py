n, m = map(int, input().split())

a, b = [0] * n, [0] * n
c, d = [0] * m, [0] * m
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(m):
    c[i], d[i] = map(int, input().split())
for i in range(n):
    ans = 0
    min = 10 ** 20
    for j in range(m):
        dis = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if min > dis:
            min = dis
            ans = j + 1
    print(ans)