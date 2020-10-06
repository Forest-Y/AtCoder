N, M, Q = map(int, input().split())
flag = [[False] * M for _ in range(N)]
cnt = [N] * M

def calc_score(i):
    ans = 0
    for j in range(M):
        if flag[i - 1][j] == True:
            ans += cnt[j]
    return ans

for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 2:
        cnt[s[2] - 1] -= 1
        flag[s[1] - 1][s[2] - 1] = True
    else:
       print(calc_score(s[1]))
