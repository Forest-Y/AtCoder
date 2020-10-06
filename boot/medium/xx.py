s = input()
i = 0
while 1:
    if s[i:] == "FESTIVAL":
        break
    i += 1
print(s[: i])