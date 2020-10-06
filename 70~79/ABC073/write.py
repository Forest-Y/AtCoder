from collections import defaultdict

n = int(input())
data = defaultdict(int)

for i in range(n):
    a = int(input())
    data[a] += 1

ans = 0
for v in data.values():
    if v % 2 == 1:
        ans += 1

print(ans)
