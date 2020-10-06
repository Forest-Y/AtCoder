n, m, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1 - 1].append(v2 - 1)
    g[v2 - 1].append(v1 - 1)

c = list(map(int, input().split()))

def change_color(x, g, i):
    for x in g:
        c[x] = c[i]

ans = []
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        ans.append(c[s[1] - 1])
        change_color(c, g[s[1] - 1], s[1] - 1)
    else:
        ans.append(c[s[1] - 1])
        c[s[1] - 1] = s[2]
for i in ans:
    print(i)