from collections import Counter
n = int(input())

def prime_factorize(num):
    a = []
    while num % 2 == 0:
        a.append(2)
        num //= 2
    
    f = 3
    while f * f <= num:
        if num % f == 0:
            a.append(f)
            num //= f
        else:
            f += 2
        
    if num != 1:
        a.append(num)
    return a

        
fac = Counter(prime_factorize(n))
ans = 0
for i in fac.keys():
    for j in range(1, fac[i] + 1):
        if fac[i] < j:
            break
        fac[i] -= j
        ans += 1

print(ans)
