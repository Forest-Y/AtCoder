x, k, d = map(int, input().split())

if x < 0:
    flag = -1
else:
    flag = 1

if abs(x) >= k * d:
    ans = x - k * d * flag
else:
    k -= abs(x) // d
    x = abs(x) % d * flag
    ans = x if k % 2 == 0 else x - d * flag

print(abs(ans))
