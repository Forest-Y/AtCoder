n = int(input())
x = 26
i = 1
ans = []
while n != 0:
    ans.append(chr(ord("a") + (n - 1) % x))
    n = (n - 1) // x

print("".join(ans[::-1]))