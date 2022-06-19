def giaithua(n):
    giaithua = 1
    if (n == 0) :
        print('Giai thừa của 0 là 0')
    else:
        for i in range(1, n + 1):
            giaithua = giaithua * i
        return giaithua
 
n = int(input("Nhập số nguyên dương n = "))
print("Giai thừa của", n , "là", giaithua(n))
