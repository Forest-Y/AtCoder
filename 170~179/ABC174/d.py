n = int(input())
s = list(input())
ans = 0
cnt_w = s.count("W")
j = 1
for i in range(n - cnt_w):
    if s[i] == "W":
        while s[-j] == "W":
            j += 1
        s[i] = "R"
        s[-j] = "W"
        ans += 1


print(ans)        