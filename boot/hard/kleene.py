n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            cnt2 += 1
print(((cnt1 * k + cnt2 * k * (k - 1) // 2)) % (10 ** 9 + 7))