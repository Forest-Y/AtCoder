from collections import defaultdict

s = ["AC", "WA", "TLE", "RE"]
n = int(input())
cnt = defaultdict(int)
for i in range(n):
    x = input()
    cnt[x] += 1

for i in range(4):
    print(s[i], "x", cnt[s[i]])