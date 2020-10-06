r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

s = [list(input()) for _ in range(r)]
dist = [[0] * c for _ in range(r)]

queue = [(sx - 1, sy - 1)]

while len(queue) > 0:
    y, x = queue.pop(0)
    if x == gx - 1 and y == gy - 1:
        print(dist[gy - 1][gx - 1])
        exit()
    
    for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        h, w = y + j, x + i
        if 0 <= h < r and 0 <= w < c:
            if s[h][w] == "." and dist[h][w] == 0:
                dist[h][w] = dist[y][x] + 1
                queue.append([h, w])
