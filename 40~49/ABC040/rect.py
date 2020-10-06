from math import sqrt
n = int(input())

ans = 10 ** 6
for i in range(1, int(sqrt(n)) + 1):
    one = n // i
    ans = min(ans, abs(i - one) + n % (i * one))

print(ans)