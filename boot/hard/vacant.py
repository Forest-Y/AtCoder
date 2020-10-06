n = int(input())
l, r = 0, n - 1
print(0)
data1 = input()
print(n - 1)
data2 = input()

def check(l, r, data1, data2):
    if ( (r - l) % 2 == 0 and data1 != data2) or ( (r - l) % 2 == 1 and data1 == data2):
        return True
    return False

while data1 != "Vacant" and data2 != "Vacant":
    m = (l + r) // 2
    print(m)
    s = input()
    if s == "Vacant":
        exit()
    if check(m, r, data1, s):
        l = m
        data1 = s
    elif check(l, m s, data1):
        r = m
        data2 = s
    
    
