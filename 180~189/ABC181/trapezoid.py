n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += (a + b) / 2 * (b - a + 1)
print(int(ans))
