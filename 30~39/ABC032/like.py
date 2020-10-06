a, b, n = [int(input()) for _ in range(3)]

while 1:
    if n % a == 0 and n % b == 0:
        print(n)
        exit()
    n += 1