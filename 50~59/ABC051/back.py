sx, sy, tx, ty = map(int, input().split())

if sx < tx:
    flag1 = -1
else:
    flag1 = 1

if sy < ty:
    flag2 = 1
else:
    flag2 = -1

def print_root(x1, y1, x2, y2):

    if y1 < y2:
        print("U" * (y2 - y1), end = "")
    else:
        print("D" * (y1 - y2), end = "")

    if x1 < x2:
        print("R" * (x2 - x1), end = "")
    else:
        print("L" * (x1 - x2), end = "")
    
print_root(sx, sy, tx, ty)
print_root(tx, ty, sx, sy)

print_root(sx, sy, sx + flag1, sy)
print_root(sx + flag1, sy, tx, ty + flag2)
print_root(tx, ty + flag2, tx, ty)

print_root(tx, ty, tx - flag1, ty)
print_root(tx - flag1, ty, sx, sy - flag2)
print_root(sx, sy - flag2, sx, sy)
print()