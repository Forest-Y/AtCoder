H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
ans = 0
def bfs(dist, s, queue):
    ret = 0
    while len(queue) > 0:
        y, x = queue.pop(0)
        for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            h, w = y + i, x + j
            if 0 <= h < H and 0 <= w < W:
                if s[h][w] == "." and dist[h][w] == -1:
                    dist[h][w] = dist[y][x] + 1
                    queue.append([h, w])
    for i in range(H):
        ret = max(ret, max(dist[i]))
    return ret

for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            queue = [(i, j)]
            ans = max(ans, bfs(dist, s, queue))

print(ans)