n = int(input())
ng = []
for i in range(3):
    x = int(input())
    ng.append(x)
cnt = 0
for i in range(100):
    print(n, n in ng)
    if n in ng:
        print("NO")
        exit()
    
    if n - 3 not in ng:
        n -= 3
    elif n - 2 not in ng:
        n -= 2
    else:
        n -= 1

print("YES" if n <= 0 else "NO")