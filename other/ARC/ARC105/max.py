from math import gcd
n = int(input())
a = list(map(int, input().split()))

a = list(set(a))
ans = a[0]
for i in range(len(a)):
    ans = gcd(ans, a[i])

print(ans)

