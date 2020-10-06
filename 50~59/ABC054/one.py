from collections import defaultdict

n, m = map(int, input().split())
a, b = [0] * m, [0] * m

for i in range(m):
    a[i], b[i] = map(int, input().split())
ans = 0
for i in range(m):
    if a[i] == 1:
        start = b[i]
        flags = defaultdict(int)
        flags[1] = 1
        flags[start] = 1
        while 1:
            #print(a.count(start))
            if len(flags) == n or (b.count(start) == 0 and a.count(start) == 0):
                break
            elif a.count(start) != 0:
                start = b[a.index(start)]
            elif b.count(start) != 0:
                start = a[b.index(start)]
            flags[start] += 1
        #print(flags, len(flags))
        if max(flags.values()) == 1 and len(flags) == n:
            ans += 1

print(ans)