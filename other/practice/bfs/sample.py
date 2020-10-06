H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
visited = [[0] * W for _ in range(H)]
queue = []

for i in range(H):
    for j in range(W):
        if c[i][j] == "s":
            queue.append([i, j])
            visited[i][j] = 1


while len(queue) > 0:
    n_h, n_w = queue.pop(0)
    if c[n_h][n_w] == "g":
        print("Yes")
        exit()

    for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        h, w = n_h + i, n_w + j
        if 0 <= h < H and 0 <= w < W:
            if c[h][w] == "." and visited[h][w] == 0:
                visited[h][w] = 1
                queue.append([h, w])

print("No")