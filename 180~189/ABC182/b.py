
n = int(input())
a = list(map(int, input().split()))
ans = 0
ans_cnt = 0
for i in range(2, max(a) + 1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if ans_cnt <= cnt:
        ans = i
        ans_cnt = cnt


print(ans)