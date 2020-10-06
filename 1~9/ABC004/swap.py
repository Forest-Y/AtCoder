s = list("123456")
n = int(input())

for i in range(n % 30):
    s[i % 5], s[i % 5 + 1] = s[i % 5 + 1], s[i % 5]

print("".join(s))