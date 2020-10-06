
n, k = map(int, input().split())

print(((n - k) * 6 * (k - 1) + 3 * (n - 1) + 1) / (n ** 3))