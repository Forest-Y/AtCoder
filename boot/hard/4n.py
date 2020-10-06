N = int(input())


for h in range(1, 3500):
    for n in range(1, 3500):
        x = 4 * h * n - N * h - N * n
        if x != 0:
            w = N * h * n / (4 * h * n - N * h - N * n)
            if int(w) == w and w > 0:
                print(h, n, int(w))
                exit()
