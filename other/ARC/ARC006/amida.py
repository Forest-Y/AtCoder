n, l = map(int, input().split())
amida = [input() for _ in range(l)]
goal = input()

for i in range(0, (n - 1) * 2 + 1, 2):
    x = i
    for j in range(l):
        if amida[j][max(x - 1, 0)] == "-":
            x -= 2
        elif amida[j][min(x + 1, (n - 1) * 2)] == "-":
            x += 2
    if goal[x] == "o":
        print((i + 2) // 2)
        exit()
