from sys import setrecursionlimit
setrecursionlimit(10000)

n, m = map(int, input().split())
ans = 0
a, b = [0] * m, [0] * m
for i in range(m):
  a[i], b[i] = map(int, input().split())

dest = [[] for _  in range(n)]
for i in range(m):
  dest[a[i] - 1].append(b[i] - 1)

def dfs(start):
  if visited[start]:
    return
  
  visited[start] = 1

  for next in dest[start]:
    dfs(next)


for i in range(n):
  visited = [0] * n
  dfs(i)
  ans += sum(visited)

print(ans)