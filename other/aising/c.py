n = int(input())
ans = [0] * n
for x in range(1, int(n ** 0.5) + 1):
    for y in range(1, int(n ** 0.5) + 1):
        for z in range(1, int(n ** 0.5) + 1):
            res = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if res <= n:
                ans[res - 1] += 1
            elif res > n:
                break

for x in ans:
    print(x)