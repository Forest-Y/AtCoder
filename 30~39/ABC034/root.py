from math import factorial
w, h = map(int, input().split())
mod = 10 ** 9 + 7

def calc(n, r):
    x, y = 1, 1
    for i in range(r):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    return x * pow(y, mod - 2, mod) % mod
print(calc(w + h - 2, w - 1))