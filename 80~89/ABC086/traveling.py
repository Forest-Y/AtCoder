
n = int(input())

data = []
data.append([0, 0, 0])
for i in range(n):
    t, x, y = map(int,  input().split())
    data.append([t, x, y])

for i in range(1, n + 1):
    dis = abs(data[i][1] - data[i - 1][1]) + abs(data[i][2] - data[i- 1][2])
    dif = data[i][0] - data[i - 1][0]
    if (dif % 2 != dis % 2 or dis > dif):
        print("No")
        exit() 

print("Yes")