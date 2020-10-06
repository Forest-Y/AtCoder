
s = input()
ban = "aiueo"

for i in range(len(s)):
    if s[i] not in ban:
        print(s[i], end = "")

print()