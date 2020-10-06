n = int(input())
s = input()
ans = 0
for i in range(n):
    if s[i] == "A":
        ans += 4
    elif s[i] == "B":
        ans += 3
    elif s[i] == "C":
        ans += 2
    elif s[i] == "D":
        ans += 1

print(ans / n)