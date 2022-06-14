def ptbac2(a,b,c) :
    if  a == 0 :
        if b ==0 :
            print('Pt vô nghiệm')
        else :
            print("Phương trình có một nghiệm: x = ", + (-c / b))
    else :
        d = b*b - 4*a*c
        if d < 0 :
            print(' Phương trình vô nghiệm')
        elif d == 0 :
            nghiem =  -b/2*a
            print('Phương trình có nghiệm là ' + str(nghiem) )
        else :
            x1 =(-b + math.sqrt(d))/2*a
            x2 =(-b - math.sqrt(d))/2*a
            print('Phương trình có 2 nghiệm' )
            print( 'x1 =' + str(x1) )
            print( 'x2 =' + str(x2) )
import math
print('Nhập a b c')
a = float(input('nhập a = '))
b = float(input('nhập b = '))
c = float(input('nhập c = '))
ptbac2(a, b, c)