import math
print('Nhập a b c')
a = int(input('nhập a = '))
b = int(input('nhập b = '))
c = int(input('nhập c = '))
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