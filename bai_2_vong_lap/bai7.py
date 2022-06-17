def songuyento(n) :
    f = 1
    if (n <2):
        f = 0
        return f 
    for p in range(2, n):
        if n % p == 0:
            f = 0
            break
    return f

n = int(input(">> nhap so tu nhien: "))
check = songuyento(n)
 
if check == 1:
    print(n," la so nguyen to")
else:
    print(n,"khong phai so nguyen to")