s = input()
t = input()
ans = []
if len(s) < len(t):
    print("UNRESTORABLE")
    exit()

for i in range(len(s) - len(t) + 1):
    prot = list(s)
    flag = True
    for j in range(len(t)):
        if prot[i + j] != t[j] and prot[i + j] != "?":
            flag = False
            break
        prot[i + j] = t[j]


    if flag == True:
        prot = "".join(prot).replace("?", "a")
        ans.append(prot)

if ans == []:
    print("UNRESTORABLE")
else:
    ans = sorted(ans)
    print(ans[0])
