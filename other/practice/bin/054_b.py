p = float(input())
l = 0
r = 100
ans = p

def calc_time(c):
    return c + p * pow(0.5, c / 1.5)
cnt = 1000
i = 0
while i < cnt:
    c1 = (l * 2 + r) / 3
    c2 = (l + r * 2) / 3
    if calc_time(c1) > calc_time(c2):
        l = c1
    else:
        r = c2
    #print(c1, c2)
    #print(r - l)
    i += 1

print(calc_time((r + l) / 2))