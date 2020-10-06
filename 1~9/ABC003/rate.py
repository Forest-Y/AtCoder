n, k = map(int, input().split())
r = list(map(int, input().split()))
r = sorted(r, reverse = True)
r = sorted(r[: k])
ans = 0
for i in range(k):
    ans = (ans + r[i]) / 2
print(ans)