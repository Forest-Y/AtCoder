
n = int(input())
x = list(map(int, input().split()))

data = sorted(x)
under = data[n // 2 - 1]
over = data[n // 2]
for i in range(n):
    if x[i] <= under:
        print(over)
    else:
        print(under)
