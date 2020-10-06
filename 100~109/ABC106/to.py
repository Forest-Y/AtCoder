
s = input()
n = int(input())

i = 0
while i != len(s) and s[i] == '1':
    i += 1

if n <= i:
    print(1)
else:
    print(s[i])