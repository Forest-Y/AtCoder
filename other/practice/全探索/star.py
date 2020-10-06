from collections import defaultdict

m = int(input())
x_y_1 = [tuple(map(int, input().split())) for _ in range(m)]
n = int(input())
x_y_2 = [tuple(map(int, input().split())) for _ in range(n)]
exist = set(x_y_2)
x_y_1.sort(), x_y_2.sort()
dis = defaultdict(int)
for i in range(n):
    dx = x_y_2[i][0] - x_y_1[0][0]
    dy = x_y_2[i][1] - x_y_1[0][1]
    cnt = 0
    for j in range(m):
        if (x_y_1[j][0] + dx, x_y_1[j][1] + dy) in exist:
            cnt += 1
        else:
            break
    if cnt == m:
        print(dx, dy)
        exit()
