print('Nhập 4 số abcd')
a = input('Nhập a ')
b = input('Nhập b ')
c = input('Nhập c ')
d = input('Nhập d ')
x = [float(a),float(b),float(c),float(d)]
solonhat = 0
for i in x :
    print(str(i))
    if i > solonhat :
        solonhat = i
        print(str(solonhat))
print('Số lớn nhất là ' + str(solonhat))