def kiemtrasonguyento(n) :
    if (n <2):
        print(str(n) + ' khong phai la so nguyen to')
        return
    thoat = False    
    for p in range(2, n):
        if n % p == 0:
            print(str(n) + ' khong phai la so nguyen to')
            thoat = True
            break

    if thoat != True :
         print(str(n) + ' la so nguyen to')
    return
    