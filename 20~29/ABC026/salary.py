n = int(input())
data = [[] for _ in range(n)]
for i in range(n - 1):
    b = int(input())
    data[b - 1].append(i + 1)
#print(data)
def calc_salary(data, cur):
    salary = []
    if len(data[cur]) == 0:
        return 1
    for chi in data[cur]:
        salary.append(calc_salary(data, chi))

    return min(salary) + max(salary) + 1
print(calc_salary(data, 0))