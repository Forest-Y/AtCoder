n = int(input())
x = n // 500

print(x * 1000 + (n - x * 500) // 5 * 5)