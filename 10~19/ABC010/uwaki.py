sx, sy, gx, gy, t, v = map(int, input().split())
from math import sqrt
n = int(input())
flag = False

def calc_dis(sx, sy, gx, gy):
    return sqrt((sx - gx) ** 2 + (sy - gy) ** 2)

for i in range(n):
    x, y = map(int, input().split())
    dis = calc_dis(sx, sy, x, y) + calc_dis(x, y, gx, gy)
    if dis <= t * v:
        flag = True

print("YES" if flag else "NO")