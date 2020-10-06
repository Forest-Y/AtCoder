s = input()
s_list = list(s)
s_list[0] = s[0].upper()
for i in range(1, len(s_list)):
    s_list[i] = s_list[i].lower()
print("".join(s_list))