n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
a = sorted(a)
for i in range(n):
    if a[i] <= x:
        ans += 1
    x -= a[i]
    
    if x <= 0:
        break

if x > 0 and ans != 0:
    ans -= 1

print(ans)