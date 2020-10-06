takahashi = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
n = int(input())
w = list(input().split())
ans = 0
for i in range(n):
    for j in range(3):
        if i != n - 1:
            if w[i] == takahashi[j]:
                ans += 1
        else:
            if w[i] == takahashi[j] + ".":
                ans += 1

print(ans)