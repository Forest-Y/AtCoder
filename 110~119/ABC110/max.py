
a, b, c = map(int, input().split())
print(max(a, b, c) * 10 + a + b + c - max(a, b, c))