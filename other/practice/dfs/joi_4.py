import sys
sys.setrecursionlimit(10 ** 6)
m = int(input())
n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
ans = 0

def dfs(i, j, visited_list, depth):
    cnt = 0
    global ans
    for p, q in ([0, 1], [1, 0], [0, -1], [-1, 0]):
        h, w = i + p, j + q
        if h < 0 or h >= n or w < 0 or w >= m:
            continue
        if visited_list[h][w] == 0 and a[h][w] == 1:
            visited_list[h][w] = 1
            dfs(h, w, visited_list, depth + 1)
            cnt += 1
            visited_list[h][w] = 0
    if cnt == 0:
        """
        print(depth)
        for k in range(n):
            print(visited_list[k])
        print()
        """
        ans = max(ans, depth)
        
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            #print(i, j)
            visited_list = [[0] * m for _ in range(n)]
            visited_list[i][j] = 1
            dfs(i, j, visited_list, 1)
    
print(ans)