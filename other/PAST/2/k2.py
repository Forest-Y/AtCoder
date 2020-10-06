n, q = map(int, input().split())
a = [[] for _ in range(n)]
for i in range(n):
    a[i].append(i + 1)

for i in range(q):
    f, t, x = map(int, input().split())
    j = a[f - 1].index(x)
    a[t - 1] += a[f - 1][j:]
    a[f - 1] = a[f - 1][:j]

for i in range(n):
    for j in range(n):
        if i + 1 in a[j]:
            print(j + 1)
            break