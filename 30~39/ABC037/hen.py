n, q = map(int, input().split())
a = [0] * n

def change_a(a, l, r, t):
    for i in range(l, r + 1):
        a[i] = t

for i in range(q):
    l, r, t = map(int, input().split())
    change_a(a, l - 1, r - 1, t)

for i in range(n):
    print(a[i])