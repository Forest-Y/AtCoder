
s = input()
tone = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]
color = "WBWBWWBWBWBW"

for i in range(len(color)):
    flag = True
    for j in range(len(s)):
        if s[j] != color[(i + j) % len(color)]:
            flag = False
            break
    
    if flag:
        print(tone[i])
        exit()