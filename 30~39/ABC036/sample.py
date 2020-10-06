from collections import defaultdict

n = int(input())
data = defaultdict(int)
a = [0] * n
for i in range(n):
    a[i] = int(input())
    data[a[i]] = 0
data = sorted(data)
ans = defaultdict(int)
i = 0
for k in data:
    ans[k] = i
    i += 1
#print(data)
for i in range(n):
    print(ans[a[i]])
