
n = int(input())

def S(n):
    ret = 0
    while n != 0:
        ret += n % 10
        n = n // 10
    return ret

print("Yes" if n % S(n) == 0 else "No")