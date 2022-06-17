import bai7
n = int(input('Nhap so cuoi cua day so muon kiem tra'))
for i in range(n) :
    kq = bai7.songuyento(i)
    if kq == 1 :
        print(str(i) + ' la so nguyen to')
    else :
        print(str(i) + ' khkong phai la so nguyen to')
