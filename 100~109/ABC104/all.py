
d, g = map(int, input().split())

p = [0] * d
c = [0] * d
for i in range(d):
    p[i], c[i] = map(int, input().split())

sum1 = 0
ans1 = 0
for i in range(d - 1, -1, -1):
    if g - sum1 < p[i] * 100 * (i + 1):
        ans1 += -(-(g - sum1) // (100 * (i + 1)))
        break
    else:
        sum1 += p[i] * 100 * (i + 1) + c[i]
        ans1 += p[i]
    if sum1 >= g:
        break
sum2 = 0
ans2 = 0
for i in range(d):
    if g - sum2 < p[i] * 100 * (i + 1):
        ans2 += -(-(g - sum2) // (100 * (i + 1)))
        break
    else:
        sum2 += p[i] * 100 * (i + 1) + c[i]
        ans2 += p[i]
    if sum2 >= g:
        break
print(min(ans1, ans2))