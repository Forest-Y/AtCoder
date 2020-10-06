import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, q = map(int, input().split())
cnt = [0] * n
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

for i in range(q):
    p, x = map(int, input().split())
    cnt[p - 1] += x

def dfs(cur, par):
    for chi in tree[cur]:
        if chi == par:
            continue
        cnt[chi] += cnt[cur]
        dfs(chi, cur)
dfs(0, -1)
print(*cnt)