n, k = map(int, input().split())
s = input()

ans = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        ans += 1

print(min(ans + 2 * k, n - 1))