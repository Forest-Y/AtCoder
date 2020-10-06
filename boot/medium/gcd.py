from collections import defaultdict
n, p = map(int, input().split())
cnt = defaultdict(int)
if n == 1:
    print(p)
    exit()
for i in range(2, int(p ** 0.5) + 1):
    flag = False
    while p % i == 0:
        p //= i
        cnt[i] += 1
ans = 1
print(cnt)
for k, v in cnt.items():
    ans *= k ** (v // n)

print(ans)