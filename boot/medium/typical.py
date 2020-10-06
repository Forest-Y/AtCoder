n, m = map(int, input().split())
flag = [True] * (n + 1)
cnt = [0] * (n + 1)
for i in range(m):
    a = int(input())
    flag[a] = False

for i in range(n, -1, -1):
    if flag[i]:
        if i == n or i == n - 1:
            cnt[i] = 1
        else:
            cnt[i] = (cnt[i + 1] + cnt[i + 2]) % (10 ** 9 + 7)
    else:
        cnt[i] = 0
print (cnt[0])