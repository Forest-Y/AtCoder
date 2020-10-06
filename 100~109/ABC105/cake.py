
n = int(input())
flag = False
for i in range(-(-n // 4) + 1):
    for j in range(-(-n // 7) + 1):
        if n == 4 * i + j * 7:
            flag = True
            break

print("Yes" if flag == True else "No")
