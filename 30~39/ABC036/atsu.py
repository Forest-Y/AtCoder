from collections import defaultdict

n = int(input())
data = defaultdict(int)
a = [0] * n
for i in range(n):
    a[i] = int(input())
b = sorted(set(a))
for i, k in enumerate(b):
    data[k] = i

for i in range(n):
    print(data[a[i]])