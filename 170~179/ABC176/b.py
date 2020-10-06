n = list(input())
ans = "Yes"
cnt = 0
for i in range(len(n)):
    cnt += eval(n[i])
print("Yes" if cnt % 9 == 0 else "No")
