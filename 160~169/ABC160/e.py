
x, y, a, b, c = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse = True)
q.sort(reverse = True)
for i in range(x):
    r.append(p[i])

for i in range(y):
    r.append(q[i])

r.sort(reverse = True)

ans = 0
for i in range(x + y):
    ans += r[i]

print(ans)