h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = [0] * (h * w)
index = 0
for i in range(n):
    for j in range(index, index + a[i]):
        ans[j] = i + 1
        index += 1

for i in range(h):
    row = ans[i * w: (i + 1) * w]
    if i % 2 == 1:
        row = row[::-1]
    for x in row:
        print(x, end = " ")
    print()