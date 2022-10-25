a = float(input('Nhập a : '))
b = float(input('Nhập b : '))
m = float(input('Nhập m : '))
if a == 0 :
    if b == 0 : 
        print('Phương trình vô nghiệm .')
    elif b != 0 :
        y = m/b 
        print('x có vố số nghiệm, y có nghiệm là ' + str(y))
elif b == 0 :
    if a == 0 :
        print('Phương trình vô nghiệm .')
    elif a != 0 :
        x = m/a 
        print('x có vố số nghiệm, y có nghiệm là ' + str(y))
else :
    print('AVENGER END GAME !')