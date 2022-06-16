# cho 1 mảng 10 số, tìm số lớn nhất
x = [10,20,120,40]
solonhat = 0
for i in x :
    print(str(i))
    if i > solonhat :
        solonhat = i
        print(str(solonhat))
print('Số lớn nhất là ' + str(solonhat))
tong = 0
for i in x :
    tong = tong + i
tbc = tong/4
print('Tổng bằng ' + str(tong))
print('Trung bình cộng là ' + str(tbc))
