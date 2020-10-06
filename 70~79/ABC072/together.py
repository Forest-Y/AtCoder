from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)

for i in range(n):
    cnt[a[i] - 1] += 1
    cnt[a[i] + 1] += 1
    cnt[a[i]] += 1

print(max(cnt.values()))
