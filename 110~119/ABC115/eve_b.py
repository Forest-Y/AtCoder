
n = int(input())
ans = 0
high = 0
for i in range(n):
    p = int(input())
    ans += p
    high = max(high, p)

print(int(ans - high / 2))