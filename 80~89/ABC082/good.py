from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)
for i in range(n):
    dic[a[i]] += 1
ans = 0
for k, v in dic.items():
    if k < v:
        ans += v - k
    elif v < k:
        ans += v

print(ans)
