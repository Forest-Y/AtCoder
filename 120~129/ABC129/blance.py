
n = int(input())

data = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += data[i]

ans = abs(sum1 - sum2)

for i in range(n):
    sum1 -= data[i]
    sum2 += data[i]
    if abs(sum1 - sum2) < ans:
        ans = abs(sum1 - sum2)

print(ans)