s = input()
choku = "choku"
for i in range(len(s)):
    if s[i] not in choku:
        print("NO")
        exit()
    
    if s[i] == "c":
        if s[i + 1] != "h":
            print("NO")
            exit()
    elif s[i] == "h":
        if s[i - 1] != "c":
            print("NO")
            exit()
print("YES")