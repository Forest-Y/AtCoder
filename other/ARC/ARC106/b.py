n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c, d = [0] * m, [0] * m
flag = [0] * n
for i in range(m):
    c[i], d[i] = map(int, input().split())
    flag[c[i] - 1] = 1
    flag[d[i] - 1] = 1
cnt1, cnt2 = 0, 0
for i in range(n):
    if flag[i] == 1:
        cnt1 += a[i]
        cnt2 += b[i]
    elif a[i] != b[i]:
        print("No")
        exit()

print("Yes" if cnt1 == cnt2 else "No")