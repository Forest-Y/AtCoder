s = input()
s_cnt, t_cnt = 0, 0
"""
ans = 0
for i in range(len(s)):
    if s[i] == "S":
        s_cnt += 1
    else:
        t_cnt += 1
        if i == len(s) - 1 or s[i + 1] == "S":
            ans += min(t_cnt, s_cnt)
            t_cnt = 0
            s_cnt = max(0, s_cnt - t_cnt)

print(len(s) - ans * 2)
"""
n = len(s)
ans = []
for i in range(n):
    if s[i] == "S":
        ans.append(s[i])
    else:
        if ans == [] or ans[-1] != "S":
            ans.append(s[i])
        else:
            ans.pop()
print(len(ans))