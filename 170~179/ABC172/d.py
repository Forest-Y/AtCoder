n = int(input())
print()

def fac(n):
    x = n
    cnt = 0
    if n < 2:
        return 1
    arr = [1]
    for i in [2, 3]:
        while (n % i == 0):
            arr.append(i)
            n = n / i
    i, add = 5, 2
    while (n >= i * i):
        while (n % i == 0):
            arr.append(i)
            n = n / i
        i = i + add
        add = 6 - add

    if (n > 1):
        arr.append(n)
    else:
        arr.append(x)
    print(arr)
    return len(arr)

def f(n):
    ret = 0
    for i in range(1, n + 1):
        x = fac(i)
        print(i, x)
        ret += x * i
    return ret

print(f(n))