n = int(input())

t, a = map(int, input().split())
x = list(map(int, input().split()))
mini = abs(a - (t - x[0] * 0.006))
ans = 1
for i in range(0, n):
    print(abs(a - (t - x[i] * 0.006)))
    if mini > abs(a - (t - x[i] * 0.006)):
        mini = abs(a - (t - x[i] * 0.006))
        ans = i + 1

print(ans)