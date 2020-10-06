
n, x = map(int, input().split())
def make_burger(n):
    if n == 0:
        return "P"
    else:
        L = make_burger(n - 1)
        return "B" + L + "P" + L + "B"
    
def calc_len(n):
    if n == 0:
        return 1
    else:
        return calc_len(n - 1) * 2 + 3


def calc_p(n):
    if n == 0:
        return 1
    else:
        return calc_p(n - 1) * 2 + 1

h = calc_len(n)
ans = 0
b = "BPPPB"
print(h)
while x >= 5:
    if x >= h / 2:
        ans += h // 4
        x -= h // 2
        h = (h - 3) / 2
        print("OK")
        print(x, h)
    
print("OK!")
for i in range(n - 1, n - x - 1, -1):
    if b[i] == "P":
        ans += 1
    
print(ans)