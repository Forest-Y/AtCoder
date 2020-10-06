n = int(input())
a = list(map(int, input().split()))

flag = False
ans = 1000
for i in range(n - 1):
    if a[i] < a[i + 1]:
        flag = True
        break

if flag:
    x = 0
    for i in range(n):
        if x == 0:
            x = ans // a[i]
            ans = ans % a[i]
        if i == n - 1 or a[i] > a[i + 1]:
            ans += x * a[i]
            x = 0
print(ans)