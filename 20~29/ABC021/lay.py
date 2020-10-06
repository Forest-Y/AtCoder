from collections import defaultdict
n =int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
cnt = defaultdict(int)

cnt[a] += 1
cnt[b] += 1
for i in range(k):
    cnt[p[i]] += 1
print("YES" if max(cnt.values()) == 1 else "NO")