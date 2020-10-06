from bisect import bisect_left
n, m = map(int, input().split())
p = [0] * (n + 1)
for i in range(n):
    p[i] = int(input())
ans = 0
data = set()
for i in range(n + 1):
    for j in range(n + 1):
        data.add(p[i] + p[j])

data = sorted(list(data))
print(data)
for i in range(len(data)):
    index = bisect_left(data, m - data[i] + 1, 0, len(data))
    #print(data[i], data[max(0, index - 1)])
    if index != 0:
        ans = max(ans, data[i] + data[max(0, index - 1)])
    #print(ans)
print(ans)