from math import pi
n = int(input())
flag = n % 2
ans = 0
r = [0] * n
for i in range(n):
    r[i] = int(input())
r.sort()
for i in range(n):
    if i % 2 != flag:
        ans += r[i] ** 2
    else:
        ans -= r[i] ** 2
print(ans * pi)