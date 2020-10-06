from collections import defaultdict
n = int(input())
cnt = [defaultdict(int) for _ in range(n)]
a = [""] * n
for i in range(n):
    a[i] = input()
    for c in a[i]:
        cnt[i][c] += 1
ans = ""
for i in range(n // 2):
    flag = False
    for k in cnt[i].keys():
        if k in cnt[n - i - 1].keys():
            ans += k
            flag = True
            break
    if flag == False:
        print(-1)
        exit()
c = ""
if n % 2 == 1:
    c = a[n // 2][0]

print(ans + c + ans[::-1])