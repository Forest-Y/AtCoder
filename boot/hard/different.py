n = int(input())
point = [0] * n
total_b = 0
for i in range(n):
    a, b = map(int, input().split())
    point[i] = a + b
    total_b += b

point.sort(reverse = True)

sum_t, sum_a = 0, 0
for i in range(n):
    if i % 2 == 0:
        sum_t += point[i]
    else:
        sum_a += point[i]

print(sum_t - total_b)
