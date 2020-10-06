from collections import defaultdict
n, k = map(int, input().split())
a = [[] for _ in range(k)]
cnt = defaultdict(int)

for i in range(k):
    d = int(input())
    a[i] = list(map(int, input().split()))

for i in range(k):
    for x in a[i]:
        cnt[x] += 1

print(n - len(cnt))