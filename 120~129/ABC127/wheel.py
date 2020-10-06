a, b = map(int, input().split())

if a <= 12 and a >= 6:
    b /= 2

print(int(b) if a >= 6 else 0)