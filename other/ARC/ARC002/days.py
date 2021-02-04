import datetime
y, m, d = map(int, input().split("/"))

d = datetime.datetime(y, m, d)

while True:
    if d.year % (d.month * d.day) == 0:
        print(d.strftime("%Y/%m/%d"))
        exit()
    d += datetime.timedelta(days = 1)