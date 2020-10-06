from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())
cnt = defaultdict(int)
for x in a:
    cnt[x] += 1
ans = [0] * q
total = sum(a)
for i in range(q):
    b, c = map(int, input().split())

    cnt[c] += cnt[b]
    total = total - b * cnt[b] + (cnt[b]) * c
    cnt[b] = 0
    ans[i] = total

for i in range(q):
    print(ans[i])