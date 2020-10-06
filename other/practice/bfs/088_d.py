h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
dist = [[0] * w for _ in range(h)]
dist[0][0] = 1
queue = [(0, 0)]
cnt = 0
while len(queue) > 0:
    n_h, n_w = queue.pop(0)
    for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        y, x = n_h + i, n_w + j
        if 0 <= x < w and 0 <= y < h:
            if s[y][x] == "." and dist[y][x] == 0:
                dist[y][x] = dist[n_h][n_w] + 1
                queue.append([y, x])

if dist[-1][-1] == 0:
    print(-1)
    exit()
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            ans += 1
    
print(ans - dist[h - 1][w - 1])
