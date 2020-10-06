n, m = map(int, input().split())
d1 = 6 * m
d2 = n % 12 * 30 + 360 / 12 * m / 60
ans = abs(d1 - d2)
print(ans if ans <= 180 else 360 - ans)