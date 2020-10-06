s = input()

format = []
for i in range(2 ** (len(s) - 1)):
    pat = ""
    for j in range(len(s) - 1):
        pat += s[j]
        if i >> j & 1:
            pat += "+"
        else:
            pat += "-"

    pat += s[-1]    
    format.append(pat)
    print(pat)

for i in range(len(format)):
    if eval(format[i]) == 7:
        print(format[i] + "=7")
        exit()