from math import sqrt
n = int(input())
ans = len(str(n))
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        ans = min(ans, max(len(str(n // i)), len(str(i))))

print(ans)