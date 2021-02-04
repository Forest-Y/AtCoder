x, y, a, b = map(int, input().split())

ans = 0
while x * (a - 1) < b and x < y:
    x *= a
    ans += 1
print((y - x - 1) // b + ans)