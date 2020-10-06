h, w, m = map(int, input().split())
cnt1, cnt2 = [0] * h, [0] * w
data = [[0] * w for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt1[a] += 1
    cnt2[b] += 1
    data[a][b] = 1
ans = sum(data[cnt1.index(max(cnt1))])
j = cnt2.index(max(cnt2))
print(cnt1, cnt2)
for i in range(h):
    ans += data[i][j]
print(ans if j != k else ans - 1)    
