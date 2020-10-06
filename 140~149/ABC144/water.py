import math 
a, b, x = map(int, input().split())

if x <= a ** 2 * b / 2:
    bottom = (x * 2 / (a * b))
    hype = math.sqrt(bottom ** 2 + b ** 2)
    print(math.degrees(math.atan2(b, bottom)))
else:
    x = a ** 2 * b - x
    height = x * 2 / (a ** 2)
    print(math.degrees(math.atan2(height, a)))