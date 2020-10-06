
n = int(input())
ans = n

def calc(n, num):
    ret = 0
    while n > 0:
        ret += n % num
        n //= num
    return ret
j = 0
for i in range(n + 1):
    cc = 0
    cc += calc(i, 6)
    cc += calc(n - i, 9)
    if ans != min(ans, cc):
        ans = min(ans, cc)
        j = i

print(ans, j, n - j)

