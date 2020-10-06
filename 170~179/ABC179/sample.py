n, k = map(int, input().split())
mod = 998244353
ans = [0] * n
ans[0] = 1
s = []
for i in range(k):
    l, r = map(int, input().split())
    s.append(l)
    s.append(r)
s = list(set(s))
for i in range(n):
    for j in s:
        if i + j >= n:
            continue
        ans[i + j] += ans[i]
        ans[i + j] %= mod
print(ans)
print(ans[-1] % mod)