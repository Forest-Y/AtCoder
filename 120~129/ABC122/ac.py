
n, q = map(int, input().split())
s = input()
cnt = 0
data = [0] * (n + 1)
ans = [0] * q
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        cnt += 1
    data[i + 1] = cnt

data[n - 1] = cnt
print(data)

for i in range(q):
    l, r = map(int, input().split())

    ans[i] = data[r - 1] - data[l - 1]

for i in range(q):
    print(ans[i])