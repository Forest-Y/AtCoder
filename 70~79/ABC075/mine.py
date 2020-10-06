
h, w = map(int, input().split())

s = [list(input()) for _ in range(h)]
ans = [[0] * w for _  in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] += s[i][max(j - 1, 0):min(j + 2, w)].count("#")
        if i != 0:
            ans[i][j] += s[i - 1][max(j - 1, 0):min(j + 2, w)].count("#")
        if i != h - 1:
            ans[i][j] += s[i + 1][max(j - 1, 0):min(j + 2, w)].count("#")

        
            

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            print(s[i][j], end ="")
        else:
            print(ans[i][j], end = "")
    print()