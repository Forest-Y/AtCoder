n, a, b = map(int, input().split())
ans = 0
for i in range(n):
    s, d = input().split()
    d = int(d)
    if d < a:
        d = a
    elif b < d:
        d = b
    if s == "East":
        ans -= d
    else:
        ans += d

if ans < 0:
    print("East", -ans)
elif ans > 0:
    print("West", ans)
else:
    print(ans)