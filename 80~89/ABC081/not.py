from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1

cnt = sorted(cnt.items(), key = lambda x:x[1])
ans = 0
for i in range(len(cnt) - k):
    ans += cnt[i][1]
print(ans)

