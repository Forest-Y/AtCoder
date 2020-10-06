from math import sqrt, cos, radians
a, b, h, m = map(int, input().split())
x = h * 30
if m != 0:
    x += 30 / (60 / m)
y = m * 6
c = min(abs(x - y), 360 - abs(x - y))
#print(abs(x - y) % 180, 2 * a * b * cos(abs(x - y) % 180), cos(radians(abs(x - y) % 180)))
print(sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(c))))