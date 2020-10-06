a, r, n = map(int, input().split())

def pow_r(x, n):
    if n == 0:
        return 1
    if x > 10 ** 9:
        print("large")
        exit()
    if n % 2 == 0:
        return pow_r(x ** 2, n // 2)
    else:
        return x * pow_r(x ** 2, n // 2)
ans = a * pow_r(r, n - 1)
print(ans if ans <= 10 ** 9 else "large")