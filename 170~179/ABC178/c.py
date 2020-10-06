from math import factorial as fac
n = int(input())
mod = 10 ** 9 + 7
ans = 10 ** n
print((ans - 2 * (9 ** n) + 8 ** n) % mod)