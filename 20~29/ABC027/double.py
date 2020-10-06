n = int(input())
depth = 0

while 2 ** depth <= n:
    depth += 1

def calc(x, flag):
    cnt = 0
    while x <= n:
        x = x * 2 + flag
        flag ^= 1
        cnt += 1

        #print(x, cnt)
    print("Takahashi" if cnt % 2 == 0 else "Aoki")

if depth % 2 == 1:
    calc(1, 1)
else:
    calc(1, 0)