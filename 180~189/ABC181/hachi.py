s = input()
flag = [0] * 10
flag[0] = 2
for i in range(len(s)):
    flag[int(s[i])] += 1
if (len(s) == 1 and s[i] == "8") or (len(s) == 2 and ( (int(s[0]) * 10 + int(s[1])) % 8 == 0 or (int(s[1]) * 10 + int(s[0])) % 8 == 0)):
    print("Yes")
    exit()
for i in range(1, 10):
    if flag[i] >= 1:
        for j in range(1, 10):
            if (i == j and flag[j] >= 2) or (i != j and flag[j] >= 1):
                for k in range(1,10):
                    if (i == k == j and flag[k] >= 3) or ( ((i == k and j != k) or (j == k and i != k)) and flag[k] >= 2) or (i != k and j != k and flag[k] >= 1):
                        if(i * 100 + j * 10 + k) % 8 == 0:
                            print("Yes")
                            """
                            print((i == k == j and flag[k] >= 3), ( ((i == k and j != k) or (j == k and i != k)) and flag[k] >= 2), (i != k and j != k and flag[k] >= 1))
                            print(i, j, k)
                            """
                            exit()


print("No")
