
antenna = [0] * 5

for i in range(5):
    antenna[i] = int(input())

k = int(input())
judge = 0
for i in range(5):
    for j in range(i + 1, 5):
        if abs(antenna[i] - antenna[j]) > k:
            judge = 1
            break

print(":(" if judge == 1 else "Yay!")