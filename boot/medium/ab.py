n, a, b = map(int, input().split())
print(max(0, b * (n - 1) + a - (a * (n - 1) + b) + 1))