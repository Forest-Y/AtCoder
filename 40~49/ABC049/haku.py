s = input()
i = len(s) - 1
flag = False
while i > 0:
    flag = False
    if s[i] == "m" and s[i - 4:i + 1] == "dream":
        flag = True
        i -= 5
    elif s[i] == "e" and s[i - 4: i + 1] == "erase":
        i -= 5
        flag = True
    elif s[i] == "r":
        if s[i - 5: i + 1] == "eraser":
            flag = True
            i -= 6
        elif s[i - 6: i + 1] == "dreamer":
            flag = True
            i -= 7
    if flag == False:
        break
print("YES" if flag else "NO")