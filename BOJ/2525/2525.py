hh, mm = map(int, input().split(' '))
mm2 = int(input())
if mm + mm2 >= 60:
    hh = hh + ((mm + mm2) // 60)
    mm = (mm + mm2) % 60
else:
    mm = mm + mm2
if hh >= 24:
    hh = hh % 24
print(hh, mm)