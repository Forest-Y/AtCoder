
s = list(input())
n = int(input())

flag = 0
s1 = []
s2 = s
for i in range(n):
    Q = input()
    if Q[0] == "2":
        if Q[2] == "1":
            if flag == 1:
                s2.append(Q[4])
            else:
                s1.append(Q[4])
        else:
            if flag == 0:
                s2.append(Q[4])
            else:
                s1.append(Q[4])
    else:
        flag ^= 1
s2 = s1[::-1] + s2
print("".join(s2) if flag == 0 else "".join(s2[::-1]))
