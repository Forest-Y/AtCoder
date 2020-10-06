
n = int(input())
a = list(map(int, input().split()))

ans = 0

def div_2(n):
    ret = 0
    while n % 2 != 1:
        ret += 1
        n /= 2
    return ret

for i in range(n):
    ans += div_2(a[i])

print(ans)