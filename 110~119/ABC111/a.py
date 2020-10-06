
n = int(input())
s = str(n)

for i in range(len(s)):
    if s[i] == '1':
        print('9', end = "")
    else:
        print('1', end = "")

print()
