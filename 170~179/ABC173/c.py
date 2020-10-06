h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
cnt = 0
for i in range(h):
    cnt += c[i].count("#")
ans = 0
for bit_i in range(2 ** h):
    h_check = []
    h_cnt = 0
    for i in range(h):
        if bit_i >> i & 1:
            h_cnt += c[i].count("#")
            h_check.append(i)
    for bit_j in range(2 ** w):
        w_cnt = 0
        for j in range(w):
            if bit_j >> j & 1:
                for y in range(h):
                    if c[y][j] == "#" and  y not in h_check:
                        w_cnt += 1
        if h_cnt + w_cnt == cnt - k:
            ans += 1
print(ans)
