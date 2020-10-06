n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

data = [[] for _ in range(max(a))]
for i in range(n):
    data[a[i] - 1].append(i)

ans = 0
for i in range(len(data)):
    ans += max(0, len(data[i]) - 1)

print(ans)