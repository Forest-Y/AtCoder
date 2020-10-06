from fractions import gcd 

N, X = map(int, input().split())
x = list(map(int, input().split()))
ans = abs(X - x[0])
for i in range(1, N):
    ans = gcd(ans, abs(x[i - 1] - x[i]))

print(ans)