n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(a[i])
ans = 0
for i in range(m):
    for j in range(i + 1, m):
        sum = 0
        for k in range(n):
            sum += max(a[k][i], a[k][j])
        
        ans = max(sum, ans)

print(ans)
