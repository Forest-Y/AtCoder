n, x = map(int, input().split())
a = list(map(int, input().split()))
if a[0] > x:
    ans = a[0] - x
    a[0] = x
else:
    ans = 0
for i in range(n - 1):
    if a[i] + a[i + 1] > x:
        #print("OK3")
        diff = (a[i] + a[i + 1]) - x
        ans += diff
        a[i + 1] -= diff
    #print(a)

print(ans)