
n, m = map(int, input().split())
data = [[] for _ in range(n)]
for i in range(m):
    p, y = map(int, input().split())
    data[p - 1].append([y, i])

ans = [None] * m
for i in  range(n):
    data[i].sort()
    for j in range(len(data[i])):
        y, k = data[i][j]
        ans[k] = '0' * (6 - len(str(i + 1))) + str(i + 1) + '0' * (6 - len(str(j + 1))) + str(j + 1)

for i in range(len(ans)):
    print(ans[i])