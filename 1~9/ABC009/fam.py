n = int(input())
price = []
for i in range(n):
    x = int(input())
    price.append(x)

price = sorted(set(price), reverse = True)
print(price[1])