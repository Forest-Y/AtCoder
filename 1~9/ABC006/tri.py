n = int(input())

tri = [0] * n
for i in range(n):
    if i == 0 or i == 1:
        tri[i] = 0
    elif i == 2:
        tri[i] = 1
    else:
        tri[i] = (tri[i - 1] + tri[i - 2] + tri[i - 3]) % (10 ** 4 + 7)
print(tri[n - 1])