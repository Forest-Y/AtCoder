n, k = map(int, input().split())
a = list(map(int, input().split()))
i = 0
j = 1
pre = 0
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
k -= l - cnt
k = k % cnt
for i in range(l - cnt):
    ans = a[i]    
for i in range(k + 1):
    ans = a[pre]
    pre = ans - 1

print(ans)