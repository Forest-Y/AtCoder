from math import sqrt
a, b = input().split()

n = int(a + b)
print("Yes" if n == int(sqrt(n)) ** 2 else "No")