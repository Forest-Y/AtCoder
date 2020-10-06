
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)

a_score, b_score = 0, 0

for i in range(n):
    if i % 2 == 0:
        a_score += a[i]
    else:
        b_score += a[i]

print(a_score - b_score)