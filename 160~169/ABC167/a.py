s = input()
t = input()
s = s + t[len(t) - 1]
print("Yes" if s == t else "No")