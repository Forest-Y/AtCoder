from math import ceil
s = int(input())
y = ceil(s / (10 ** 9))

x = (10 ** 9) * y - s
print(0, 0, 10 ** 9, 1, x, y)