
s1 = list(input())
s2 = list(input())
for i in range(len(s1)):
    if s1 == s2:
        print("Yes")
        exit()
    temp = s2[0]
    for j in range(1, len(s1)):
        s2[j - 1] = s2[j]
        if j == len(s2) - 1:
            s2[j] = temp
print("No")