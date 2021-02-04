n = input()
length = len(n)
ans = length
for i in range(1, 2 ** length):
    cnt = 0
    num = ""
    for bit in range(length):
        if i >> bit & 1:
            num += n[bit]
            cnt += 1
    if int(num) % 3 == 0:
        ans = min(ans, length - cnt)
print(ans if ans != length else -1)
