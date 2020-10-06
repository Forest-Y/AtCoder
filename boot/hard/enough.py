from bisect import bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
total = [0] * n
total[0] = a[0]
for i in range(1, n):
    total[i] = total[i - 1] + a[i]
for i in range(n - 1, -1, -1):
    if total[i] < k:
        break
    index = bisect_right(total, total[i] - k, 0, n)
    ans += index + 1
print(ans)