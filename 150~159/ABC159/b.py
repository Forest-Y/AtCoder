s = input()
n = len(s)
judge = 1
for i in range(int(n / 2)):
    if s[i] != s[n - 1 - i]:
        judge = 0
        break

for i in range(int((n - 1) / 4)):
    if s[i] != s[int((n - 1) / 2 - 1 - i)]:
        judge = 0
        break

for i in range(int((n + 3) / 2), n):
    if s[i] != s[n - 1 - i]:
        judge = 0
        break

print("Yes" if judge == 1 else "No")