
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i < min(k - 1, n - k):
        #print(i + 1)
        ans += a[i] * (i + 1)
    elif i > max(n - k, k - 1):
        #print(i)
        ans += a[i] * (n - i)
    else:
        ans += a[i] * min(n - k + 1, k)
    #print(ans, i)
print(ans)