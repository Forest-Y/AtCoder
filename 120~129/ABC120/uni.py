s = list(input())
n = len(s)
i = 0
cnt = 0
while i < n - 1:
    if n == 1:
        break
    if (s[i] == '0' and s[i + 1] == '1') or (s[i] == '1' and s[i + 1] == '0'):
        s[i:i + 2] = []
        i = max(i - 1, 0)
        cnt += 2
        n = len(s)
    else:
        i += 1

print(cnt)