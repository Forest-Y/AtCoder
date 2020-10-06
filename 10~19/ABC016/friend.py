from collections import defaultdict
n, m = map(int, input().split())
friends = [[] for _ in range(n)]
ans = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)

for i in range(n):
    for j in range(len(friends[i])):
        for k in range(len(friends[friends[i][j]])):
            f_f = friends[friends[i][j]][k]
            if f_f not in ans[i] and f_f != i and f_f not in friends[i]:
                ans[i].append(f_f)

for i in range(n):
    print(len(ans[i]))