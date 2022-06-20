a = input('Nhập vào 1 số nguyên dương : ')
while int(a) < 0:
    a = input('Vui lòng nhập vào 1 số nguyên dương : ')
e = reversed(a)
print(str(e))