
import copy
n = int(input())
X = list(input())
ans = [0] * n

def calc(x, cnt):
    if cnt == 0:
        return 0
    return 1 + calc(x % cnt, popcount(x % cnt))



def popcount(x):
    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

for i in range(n):
    bit = copy.copy(X)
    if bit[i] == "0":
        bit[i] = "1"
    else:
        bit[i] = "0"
    
    x = int("".join(bit), 2)
    cnt = popcount(x)
    ans[i] = calc(x, cnt)
    

for i in ans:
    print(i)