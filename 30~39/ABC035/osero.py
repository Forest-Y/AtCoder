n, q = map(int, input().split())
ans = [0] * n
for i in range(q):
    l, r = map(int, input().split())
    ans[l - 1] += 1
    if r < n:
        ans[r] -= 1

for i in range(1, n):
    ans[i] += ans[i - 1]

#print(ans)
for i in range(n):
    print(ans[i] % 2, end = "")
print()