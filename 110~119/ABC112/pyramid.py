
n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
result = [0] * n
flag = 1

for i in range(n):
    if data[i][2] != 0:
        start = i
        break
for i in range(100 + 1):
    for j in range(100 + 1):
        flag = 1
        h = data[start][2] + abs(data[start][0] - i) + abs(data[start][1] - j)
        for k in range(n):
            if data[k][2] != max(h - abs(data[k][0] - i) - abs(data[k][1] - j), 0):
                flag = 0
                break
        if flag == 1:
            print("{0} {1} {2}".format(i, j, h))
            exit()
