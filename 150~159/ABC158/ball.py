
x, a, b = map(int, input().split())

cnt = 0
sum = 0
i = 0
if a == 0:
    print(0)
    exit()
i = x // (a + b)
cnt = i * a
sum = i * a + i * b


print(cnt + min(x - sum, a))