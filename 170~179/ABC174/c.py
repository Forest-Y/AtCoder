k = int(input())
x = 7 % k
ans = 1
for i in range(k):
    if x == 0:
        print(ans)
        exit()
    ans += 1
    x = (x * 10 + 7) % k

print(-1)
