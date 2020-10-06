
h, w = map(int, input().split())

mass = []
for i in range(h):
    s = input()
    s += "."
    mass.append(s)
mass.append("." * (w + 1))
for i in range(h):
    for j in range(w):
        if mass[i][j] == "#":
            if mass[i][j + 1] != "#" and mass[i][j - 1] != "#" and mass[i + 1][j] != "#" and mass[i - 1][j] != "#":
                print("No")
                exit()
print("Yes")