from collections import defaultdict

cnt = defaultdict(int)

for m in range(2):
    n = int(input())
    for i in range(n):
        s = input()
        if m == 0:
            cnt[s] += 1
        else:
            cnt[s] -= 1

print(max(max(cnt.values()), 0))