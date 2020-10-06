n = int(input())
s = input()

if n % 2 == 0:
    print(-1)
    exit()

t = s[n // 2]
ans = 0
while len(t) < n:
    ans += 1
    if ans % 3 == 1:
        t = "a" + t + "c"
    elif ans % 3 == 2:
        t = "c" + t + "a"
    else:
        t = "b" + t + "b"

print(-1 if s != t else ans)
