n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

ans = []
ans.append(sum(a[0]) + a[1][n - 1])
for i in range(n - 2, -1, -1):
    ans.append(ans[n - 2 - i] - a[0][i + 1] + a[1][i])

print(max(ans))