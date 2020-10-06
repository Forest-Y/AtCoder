x, y = map(int, input().split())
ans = 0
m = [300000, 200000, 100000]
if x <= 3:
    ans += m[x - 1]
if y <= 3:
    ans += m[y - 1]
if x == 1 and y == 1:
    ans += 400000

print(ans)