n, d, k = map(int, input().split())
l, r, s, t = [0] * d, [0] * d, [0]* k, [0] * k
ans = [0] * k
for i in range(d):
    l[i], r[i] = map(int, input().split())
for  i in range(k):
    s[i], t[i] = map(int, input().split())

for i in range(k):
    start = s[i]
    goal = t[i]
    for j in range(d):
        if l[j] <= start <= r[j]:
            if start > goal:
                start = max(goal, l[j])
            elif start < goal:
                start = min(r[j], goal)
        if start == goal:
            ans[i] = j + 1
            break
for i in range(k):
    print(ans[i])