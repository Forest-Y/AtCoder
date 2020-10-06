n = int(input())

passwords = [] * (n ** 3)
abc = ["a", "b", "c"]
index = 0
def set_passwords(passwords, i, password):
    global index
    if i == n:
        passwords.append("".join(password))
        index += 1
        return
    
    for j in abc:
        password.append(j)
        set_passwords(passwords, i + 1, password)
        password.pop(-1)

set_passwords(passwords, 0, [])
passwords.sort()
for i in range(len(passwords)):
    print(passwords[i])
