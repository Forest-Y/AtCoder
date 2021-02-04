n = int(input())

def calc(a, b):
    x = n
    i = 1
    while x > 0:
        x = n - a ** i
        j = 1
        while b ** j <= x:
            if b ** j == x:
                if a == 3:
                    print(i, j)
                else:
                    print(j, i)
                exit()
            j += 1
        i += 1
        


        
calc(3, 5)
calc(5, 3)
print(-1)