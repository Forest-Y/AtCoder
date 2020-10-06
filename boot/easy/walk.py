l, x, y, s, d = map(int, input().split())
dis1 = d - s if d > s else d + s
dis2 = s + (l - d) if d > s else s - d
print(dis1, dis2)
print(min(dis1 / (x + y), dis2 / (y - x)))