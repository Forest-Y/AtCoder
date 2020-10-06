from collections import deque
h, w = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())
s = [list(input()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
ans_flag = False

queue1 = deque()
queue2 = deque()
visited[c_h - 1][c_w - 1] = 1
queue1.append([c_h - 1, c_w - 1])
ans = -1
def dfs(queue1, queue2):
    global ans_flag
    while queue1:
        y, x = queue1.pop()
        if y == d_h - 1 and x == d_w - 1:
            ans_flag = True
            return 
        for i, j in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            nx = x + i
            ny = y + j
            if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] == 0:
                if s[ny][nx] != "#":
                    visited[ny][nx] = 1
                    queue1.append([ny, nx])
                else:
                    queue2.append([y, x])


dfs(queue1, queue2)
while queue2:
    m = len(queue2)
    flag = False
    for a in range(m):
        y, x = queue2.pop()
        for k in range(5):
            for i, j in ([-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2]):
                ny = y + j + k
                nx = x + i
                if 0 <= nx < w and 0 <= ny < h and visited[ny][nx] == 0 and s[ny][nx] != "#":
                    #print(ny, nx, y, x)
                    flag = True
                    queue1.append([ny, nx])
                    dfs(queue1, queue2)

    if flag:
        ans += 1
    else:
        break

print(ans + 1 if ans != -1 or ans_flag else ans)
