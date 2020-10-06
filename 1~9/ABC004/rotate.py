
c = [list(map(str, input().split())) for _ in range(4)]
for i in range(3, -1, -1):
    print(" ".join(c[i][::-1]))
