
w, h, n = map(int, input().split())
x, y, a = [0] * n, [0] * n, [0] * n

for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())
fill_area = [[0] * w for _ in range(h)]

def fill(l, r, d, u, area):
    for i in range(d, u):
        for j in range(l, r):
            if area[i][j] == 0:
                area[i][j] = 1
        
    

for i in range(n):
    if a[i] == 1:
        fill(0, x[i], 0,  h, fill_area)
    elif a[i] == 2:
        fill(x[i], w, 0, h, fill_area)
    elif a[i] == 3:
        fill(0, w, h - y[i], h, fill_area)
    else:
        fill(0, w, 0, h - y[i], fill_area)
    """
    for j in range(h):
        print(fill_area[j])
    print()
    """
#print(sum(map(sum, fill_area)))
print(h * w - sum(map(sum, fill_area)))