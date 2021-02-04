n = int(input())
a = list(map(int, input().split()))

p = [0] * n
q = [0] * n
"""
for i in a:
    p.append(p[-1] + i)
    q.append(p[-1]) if p[-1] > q[-1] else q.append(q[-1])
"""
for i in range(n):
    p[i] = p[i - 1] + a[i]
    q[i] = p[i] if p[i] > q[i - 1] else q[i - 1]
r = 0
x = 0
for i in range(n):
    r = max(r, x + q[i])
    x += p[i]

print(r)