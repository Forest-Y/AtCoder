w, h, n = map(int, input().split())

x, y, a = [0] * n, [0] * n, [0] * n

for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())

start, end  = [0, 0], [w, h]

for i in range(n):
    if a[i] == 1 and x[i] > start[0]:
        start[0] = x[i]
    elif a[i] == 2 and x[i] < end[0]:
        end[0] = x[i]
    elif a[i] == 3 and start[1] < y[i]:
        start[1] = y[i]
    elif a[i] == 4 and end[1] > y[i]:
        end[1] = y[i]
    
if (end[0] - start[0]) <= 0 or (end[1] - start[1]) <= 0:
    print(0)
else:
    print( (end[0] - start[0]) * (end[1] - start[1]))