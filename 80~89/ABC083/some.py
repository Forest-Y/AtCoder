
n, a, b = map(int, input().split())
ans = 0

def calc_sum(i):
    ret = 0
    while i != 0:
        ret += i % 10
        i //= 10
    return ret

for i in range(1, n + 1):
    sum = calc_sum(i)
    if a <= sum and sum <= b:
        ans += i

print(ans)
