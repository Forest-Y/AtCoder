a, b, c, d = map(int, input().split())
if  b * c == d * a:
    print("DRAW")
else:
    print("AOKI" if b * c < d * a else "TAKAHASHI")