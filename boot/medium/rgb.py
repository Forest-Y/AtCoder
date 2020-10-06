r, g, b, n = map(int, input().split())

ans = 0
for i in range(n // r + 1):
    for j in range((n - i * r) // g + 1):
        k = n - (i * r + j * g)
        if k % b == 0:
            ans += 1

print(ans)