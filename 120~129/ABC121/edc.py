
n, m = map(int, input().split())

data = []

for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

data.sort(key = lambda x: x[0])
buy = 0
ans = 0

for i in range(n):
    buy = min(data[i][1], m)
    ans += buy * data[i][0]
    m -= buy
    if m == 0:
        break


print(ans)