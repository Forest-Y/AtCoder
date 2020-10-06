r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

C = [list(input()) for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
dist[sy - 1][sx - 1] = 0
queue = [(sy - 1, sx - 1)]
while len(queue) > 0:
    ny, nx = queue.pop(0)
    for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        y, x = ny + i, nx + j
        if 0 <= y < r and 0 <= x < c:
            if C[y][x] == "." and dist[y][x] == -1:
                dist[y][x] = dist[ny][nx] + 1
                queue.append((y, x))
print(dist[gy - 1][gx - 1]) 
