import bai7
e = int(input('Nhập số tự nhiên cuối của dãy số muốn kiểm tra : '))

for i in range(e) :
    d = bai7.songuyento(i)
    if (d == 1) :
        print(str(i) + ' la so nguyen to')
    else :
        print(str(i) + ' khong phai la so nguyen to')

