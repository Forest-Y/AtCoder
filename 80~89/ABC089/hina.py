from collections import defaultdict

cnt = defaultdict(int)

n = int(input())
s = list(input().split())
for i in range(n):
    cnt[s[i]] += 1

print("Three" if len(cnt) == 3 else "Four")