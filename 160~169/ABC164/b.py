a, b, c, d = map(int, input().split())
while a > 0 and c > 0:
    c -= b
    a -= d

if a <= 0 and c <= 0:
    print("Yes")
    exit()

print("Yes" if a > 0 else "No")
