
n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print("No War" if max(x) < min(y) and X < min(y) and min(y) < Y else "War")