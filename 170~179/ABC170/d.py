from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1
cnt = sorted(cnt.items(), key = lambda x: x[0])
ans = n
for i in range(len(cnt)):
    if cnt[i][1] != 1:
        ans -= cnt[i][1]
        continue
    for j in range(i):
        if cnt[i][0] % cnt[j][0] == 0:
            ans -= 1
            break
print(ans)