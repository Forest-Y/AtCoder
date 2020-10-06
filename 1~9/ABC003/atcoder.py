s = list(input())
t = list(input())
atcoder = "atcoder@"
for i in range(len(s)):
    if s[i] == "@" and t[i] in atcoder:
        s[i] = t[i]
    if t[i] == "@" and s[i] in atcoder:
        t[i] = s[i]
print("You can win" if s == t else "You will lose")