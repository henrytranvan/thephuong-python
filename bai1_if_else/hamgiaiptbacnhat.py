def giaiptbac1(a,b) :
    if a == 0 :
        print('Phương trình vô nghiệm')
    else :
        x = -b/a
        print('nghiệm là x = ' + str(x))

print('Nhập hai số a b')
a = float(input('nhập a = '))
b = float(input('nhập b = '))
giaiptbac1(a, b)