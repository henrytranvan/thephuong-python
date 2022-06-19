coso = int(input('Nhập cơ số : '))
luythua = int(input('Nhập lũy thừa :'))

if luythua == 0 : 
    print('Lũy thừa 0 của ' + str(coso) + 'bằng 1')
else :
    ketqua = 1;
    while (luythua!=0) :
        ketqua = ketqua*coso
        luythua = luythua-1
    print(ketqua)
