n, m, x = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

ans = -1

def calc_score(data, score):
    for i in range(m):
        score[i] += data[i + 1]

def judge_score(score):
    for i in range(m):
        if score[i] < x:
            return False
    
    return True

for i in range(2 ** n):
    score = [0] * m
    price = 0
    for j in range(n):
        if i >> j & 1:
            calc_score(data[j], score)
            price += data[j][0]
    if judge_score(score):
        if ans == -1:
            ans = price
        else:
            ans = min(ans, price)

print(ans)