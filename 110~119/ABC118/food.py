n , m = map(int, input().split())
food = [0] * m
data = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(1, data[i][0] + 1):
        food[data[i][j] - 1] += 1

ans = 0
for i in range(m):
    if food[i] == n:
        ans += 1

print(ans)