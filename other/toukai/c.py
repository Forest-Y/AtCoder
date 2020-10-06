n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * n

for i in range(k):
    for j in range(n):
        index = max(0, j - a[j])
        if (index == j and i == 0) or index != j:
            ans[index] += 1
        if j + a[j] + 1 < n:
            ans[min(n - 1, j + a[j] + 1)] -= 1
    cnt = 0
    print(ans)
    for j in range(n):
        cnt += ans[j]
        a[j] = cnt
    print(a)
