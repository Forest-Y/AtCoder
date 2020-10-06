n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]
for i in range(n):
    for j in range(n):
        if a[i][j] == b[0][0] and i + m - 1 < n and j + m - 1 < n:
            flag = 1
            for y in range(m):
                for x in range(m):
                    if a[i + y][j + x] != b[y][x]:
                        flag = 0
                        break
                
            if flag == 1:
                print("Yes")
                exit()

print("No")
