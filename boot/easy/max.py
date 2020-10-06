n = int(input())
ans1 = 0
d = [0] * n
for i in range(n):
    d[i] = int(input())
    ans1 += d[i]
total = 0
ans2 = 10 ** 10
d = sorted(d, reverse = True)
for i in range(n - 1):
    total += d[i]
    print(total)
    ans2 = min(ans2, total - (ans1 - total))

print(ans1, ans2)