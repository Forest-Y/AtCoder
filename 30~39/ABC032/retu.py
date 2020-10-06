n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
if 0 in s:
    print(n)
    exit()
ans, num, r = 0, 1, 0
for i in range(n):
    if r == n:
        break
    while num * s[r] <= k:
        num *= s[r]
        r += 1
        if r == n:
            break
    ans = max(ans, r - i)
    if i == r:
        r += 1
    else:
        num /= s[i]

print(ans)
