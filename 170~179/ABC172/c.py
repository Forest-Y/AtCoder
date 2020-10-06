
n, m, k = map(int, input().split())
from bisect import bisect_right

a = list(map(int, input().split()))
b = list(map(int, input().split()))
total_a = [0] * n
total_b = [0] * m

def set_data(data, a, x):
    data[0] = a[0]
    for i in range(1, x):
        data[i] = data[i - 1] + a[i]

set_data(total_a, a, n)
set_data(total_b, b, m)

def cnt(a, b, n, m):
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] <= k:
            index = bisect_right(b, k - a[i], 0, m)
            ans = max(ans, i + index + 1)
    return ans

print(max(cnt(total_a, total_b, n, m), cnt(total_b, total_a, m, n)))

