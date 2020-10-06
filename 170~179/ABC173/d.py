n = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
ans = a[0]
i = 1
j = 1
while i < n - 1:
    for x in range(2):
        ans += a[j]
        i += 1
        if i == n - 1:
            print(ans)
            exit()
    j += 1
print(ans)