
n = int(input())
a = list(map(int, input().split()))
calc = []
mean = 0
for i in range(n):
    calc.append(a[i] - (i + 1))
    mean += a[i] - (i + 1)

calc.sort()
b = calc[n // 2]
print(b, mean / n)
ans = 0
for i in range(n):
    ans += abs(a[i] - (b + i + 1))

print(ans)