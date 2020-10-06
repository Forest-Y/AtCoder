H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
print(s)
ans = 0

def bfs(dist, s, queue):
    while len(queue) > 0:
        y, x = queue.pop(0)
        for i, j in range([0, 1], [1, 0], [-1, 0], [0, -1]):
            h, w = y + i, x + j
            if 0 <= h < H and 0 <= w < W:
                if s[h][w] == "." and dist[h][w] == 0:
                    dist[h][w] = dist[y][x] + 1
                    queue.append([h, w])

    return max(dist)
            


for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            dist = [[0] * W for _ in range(H)]
            queue = [(s[i], s[j])]
            ans = max(ans, bfs(dist, s, queue))

print(ans)