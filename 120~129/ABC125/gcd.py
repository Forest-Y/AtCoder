from math import gcd

n = int(input())
A = list(map(int, input().split()))
L, R = [0] * (n + 1), [0] * (n + 1)

for i in range(1, n + 1):
    L[i] = gcd(L[i - 1], A[i - 1])

for i in range(n - 1, -1, -1):
    R[i] = gcd(R[i + 1], A[i])

ans = 0
#print(L, R)
for i in range(n):
    ans = max(ans, gcd(L[i], R[i + 1]))
print(ans)