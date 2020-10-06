from collections import deque
H, W = map(int, input().split())
g = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if g[i][j] == "s":
            s_x, s_y = j, i 
stack = deque([[s_y, s_x]])

visited_list = [[0] * W for _ in range(H)]
visited_list[s_y][s_x] = 1

def dfs(c, visites_list, stack):
    while len(stack) > 0:
        h, w = stack.pop()
        if c[h][w] == "g":
            return "Yes"
        
        for j, k in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            n_h, n_w = h + j, w + k
            if n_h < 0 or n_h >= H or n_w < 0 or n_w >= W:
                continue
            if c[n_h][n_w] != "#" and visited_list[n_h][n_w] == 0:
                visited_list[n_h][n_w] = 1
                stack.append([n_h, n_w])
    return "No"
print(dfs(g, visited_list, stack))
