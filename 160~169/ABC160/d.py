
n, x, y = map(int, input().split())

for i in range(1, n):
    if i == 1:
        print(n)
    elif i >= n - 2:
        print(n - 1 - i)
    else:
        if x == 1 and y == n:
            print(i)
        elif x == 1 or y == n:
            print(n - i)
        else:
            print(n + 1 - i)
