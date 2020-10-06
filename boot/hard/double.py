n = int(input())

ans = 0
if n % 2 == 0:
    x = 10
    while x <= n:
        ans += n // x
        x *= 5

print(ans)