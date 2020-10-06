from math import ceil
a, b, k, l = map(int, input().split())
print(min(k // l * b + k % l * a, a * k, ceil(k / l) * b))