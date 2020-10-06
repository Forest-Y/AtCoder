o = input()
e = input()
for i in range(len(e)):
    print(o[i] + e[i], end = "")
if len(e) < len(o):
    print(o[i + 1])
else:
    print()