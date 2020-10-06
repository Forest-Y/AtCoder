
h = int(input())

def calc_ans(h, n):
    if h == 1:
        return 2 ** n
    else:
        return 2 ** n + calc_ans(h // 2, n + 1)
print(calc_ans(h, 0))