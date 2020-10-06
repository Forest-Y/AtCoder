a, b = map(int, input().split())
if a <= 0 <= b:
    print("Zero")
elif a < b < 0:
    print("Positive" if (b - a + 1) % 2 == 0 else "Negative")
else:
    print("Positive")