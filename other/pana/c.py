from math import sqrt

a, b, c = map(int, input().split())
print(4 * a * b, (c - a - b) ** 2)
print("Yes" if 4 * a * b < (c - a - b) ** 2 and c - a - b > 0 else "No")