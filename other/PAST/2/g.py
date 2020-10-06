from collections import deque
N, X, Y = map(int, input().split())
w, h = 500, 500
X, Y = X + w // 2, Y + h // 2
g = [["."] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]
visited[0][0] = True
cnt = [[0] * w for _ in range(h)]
for i in range(N):
    x, y = map(int, input().split())
    g[h // 2 + y][w // 2 + x] = "#"

queue = deque()
queue.append((w // 2, h // 2))

def bfs(q):
    while len(q) > 0:
        nx, ny = q.popleft()
        for i, j in ([1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [0, -1]):
            x, y = nx + i, ny + j
            if 0 <= x < w and 0 <= y < h:
                if x == X and y == Y:
                    print(cnt[ny][nx] + 1)
                    exit()
                if g[y][x] == "." and visited[y][x] == False:
                    queue.append((x, y))
                    visited[y][x] = True
                    cnt[y][x] = cnt[ny][nx] + 1

    print(-1)
bfs(queue)