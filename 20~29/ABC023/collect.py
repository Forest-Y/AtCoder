R, C, K = map(int, input().split())
n = int(input())
row = [0] * R
line = [0] * C
r, c = [0] * n, [0] * n
for i in range(n):
    r[i], c[i] = map(int, input().split())
    row[r[i] - 1] += 1
    line[c[i] - 1] += 1
r_cnt, l_cnt = [0] * (K + 1), [0] * (K + 1)

ans = 0
for i in range(R):
    if row[i] <= K:
        r_cnt[row[i]] += 1
for i in range(C):
    if line[i] <= K:
        l_cnt[line[i]] += 1
for i in range(0, K + 1):
    ans += l_cnt[i] * r_cnt[K - i]
for i in range(n):
    if row[r[i] - 1] + line[c[i] - 1] == K:
        ans -= 1
    elif row[r[i] - 1] + line[c[i] - 1] == K + 1:
        ans += 1
print(ans)