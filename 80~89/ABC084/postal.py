a, b = map(int, input().split())
s = input()

for i in range(a + b + 1):
    if (i == a and s[i] != '-') or (i != a and s[i] == '-'):
        print("No")
        exit()

print("Yes")