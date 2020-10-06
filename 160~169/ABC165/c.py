
n, m, q = map(int, input().split())
a, b, c, d = [0] * q, [0] * q, [0] * q, [0] * q
score = [0] * n
ans = 0
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

def calc_score(score):
    ret = 0
    for i in range(q):
        if score[b[i] - 1] - score[a[i] - 1] == c[i]:
            ret += d[i]
    return ret

def dfs(score, i, num):
    global ans
    if i == n:
        ans = max(ans, calc_score(score))
        return 
    for j in range(num, m + 1):
        score[i] = j
        dfs(score, i + 1, j)


dfs(score, 0, 1)
print(ans)