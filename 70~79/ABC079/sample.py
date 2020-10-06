
n = int(input())
data = []

for i in range(n):
    name = input()
    data.append([name])
    
for i in range(2 ** n):
    patern = []
    for j in range(n):
        if i >> j & 1:
            patern.append(data[j])
        
    print(patern)