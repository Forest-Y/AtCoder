n, k = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 1
root = [0] * n
flag = [0] * n
while root[i] == 0:
    root[i] = j
    flag[i] = 1
    pre = i
    i = a[i] - 1
    j += 1
cnt = root[pre] - root[i] + 1
l = sum(flag)
ans = 0
if l == cnt and k % l == 0:
    print(1)
    exit()
for i in range(min(k, l - cnt)):
    ans = a[max(ans - 1, 0)]
k = (max(0, k - (l - cnt))) % cnt
for i in range(k):
    ans = a[max(0, ans - 1)]

print(ans)