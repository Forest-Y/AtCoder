

def judge_last(x):
    if x % 10 != 0 and last > x % 10:
        return x % 10
    return last

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
last = 10

last = judge_last(a)
last = judge_last(b)
last = judge_last(c)
last = judge_last(d)
last = judge_last(e)

a = -(-a // 10) * 10
b = -(-b // 10) * 10 
c = -(-c // 10) * 10
d = -(-d // 10) * 10 
e = -(-e // 10) * 10
print(a + b + c + d + e - 10 + last) 