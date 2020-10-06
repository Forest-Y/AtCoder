a, b = map(int, input().split())

ans = 0

def judge(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return 0
    return 1

for i in range(a, b + 1):
    ans += judge(str(i))

print(ans)