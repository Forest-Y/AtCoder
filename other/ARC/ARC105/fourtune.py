data = list(map(int, input().split()))
total = sum(data)
ans = "No"
for i in range(2 ** 4):
    cnt = 0
    for j in range(4):
        if i >> j & 1:
            cnt += data[j]
    if cnt == total / 2:
        ans = "Yes"
        break

print(ans)
