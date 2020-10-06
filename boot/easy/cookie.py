a, b, c = map(int, input().split())
ans = 0
if a == b == c and a % 2 == 0:
    print(-1)
else:
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        total = a + b + c
        a = (total - a) / 2
        b = (total - b) / 2
        c = (total - c) / 2
        ans += 1
    print(ans)