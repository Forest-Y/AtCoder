s = input()

if s[0] != 'A':
    print("WA")
    exit()
cnt = 0
s_list = list(s)
s_list[0] = 'a'
for i in range(2, len(s) - 1):
    if s[i] == 'C':
        s_list[i] = 'c'
        cnt += 1
if cnt != 1:
    print("WA")
    exit()
s = "".join(s_list)
for i in range(len(s)):
    if ord(s[i]) >= ord("A") and ord(s[i]) <= ord("Z"):
        print("WA")
        exit()

print("AC")
