
H, W = map(int, input().split())
h, w = map(int, input().split())

print(W * H - (h * W + H * w - h * w))