
n, m = map(int, input().split())

x = list(map(int, input().split()))
if n >= m:
    print(0)
    exit()
x.sort()
dis = [0] * (m - 1)
for i in range(m - 1):
    dis[i] = x[i + 1] - x[i]

dis.sort()
ans = x[m - 1] - x[0]
for i in range(len(dis) - 1, len(dis)- n, -1):
    ans -= dis[i]

print(ans)