
n = int(input())
s = input()
ans = s.count("R") * s.count("G") * s.count("B")
for i in range(n - 1):
    for j in range(min(i + 1, n - i)):
        if s[i] != s[i + j] and s[i] != s[i - j] and s[i + j] != s[i - j]:
            ans -= 1

print(ans)