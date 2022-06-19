print('Nhap 1 mang cac so')
ketthuc = False
ds = []
while (ketthuc != True) :
    a = input()
    if a == 'k' :
        break
    ds.append(float(a))
solonhat = 0
for i in ds :
    print(str(i))
    if int(i) > solonhat :
        solonhat = i
        print(str(solonhat))
print('Số lớn nhất là ' + str(solonhat))