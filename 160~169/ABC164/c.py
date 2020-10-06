from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for i in range(n):
    s = input()
    cnt[s] += 1

print(len(cnt))