s = input()

index = 0
cnt = 0
ans = ""
while index < len(s):
    cnt = 1
    ans += s[index]
    while index < len(s) - 1 and s[index] == s[index + 1]:
        index += 1
        cnt += 1
    print(cnt)
    index += 1
    ans += str(cnt)
print(ans)