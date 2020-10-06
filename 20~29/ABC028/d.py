
a = list(map(int, input().split()))
sum_list = []

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            if i != j != k:
                sum_list.append(a[i] + a[j] + a[k])
sum_list.sort(reverse = True)
print(sum_list[2])