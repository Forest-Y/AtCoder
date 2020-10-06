n = int(input())
a = list(map(int, input().split()))

if sum(a) % n != 0:
    print(-1)
    exit()

mean = sum(a) // n
i = 0
ans = 0
cnt = 1
total = 0
while i < n:
    total += a[i]
    if cnt != 1:
        ans += 1
    if total / cnt == mean:
        total = 0
        cnt = 0
    cnt += 1
    i += 1
print(ans)