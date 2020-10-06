a, b, x = map(int, input().split())

def calc(n):
    if n <= -1 :
        cnt = 0
    else:
        cnt = int( n // x ) + 1
    return int(cnt)
    
cnt_a = calc(a-1)
cnt_b = calc(b)

ans = cnt_b - cnt_a
print(int(ans))
