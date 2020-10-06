h, w, t = map(int, input().split())
s = [input() for _ in range(h)]
dist = [[[-1, 0] for _ in range(w)] for _ in range(h)]
goal = []
queue = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            queue.append([i, j])
            dist[i][j] = [0, 0]
            print(i, j)
            break
print(dist)
while len(queue) > 0:
    n_y, n_x = queue.pop(0)
    for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        y, x = n_y + i, n_x + j
        if 0 <= x < w and 0 <= y < h:
            """
            if s[y][x] == "G":
                goal.append([dist[n_y][n_x]])
            else:
            """
            if dist[y][x] == [-1, 0]:
                if s[y][x] == "#":
                    dist[y][x][1] = min(dist[n_y][n_x][1], dist[y][x][1]) + 1
                else:
                    dist[y][x][1] = dist[n_y][n_x][1]
                dist[y][x][0] = dist[n_y][n_x][0] + 1
                queue.append([y, x])

    for i in range(h):
        print(dist[i])
    print()

for i in range(h):
    print(dist[i])
print(goal)