print('Nhập độ dài ba cạnh :')
a = float(input('Nhập độ dài cạnh bên :'))
b = float(input('Nhập độ dài cạnh bên :'))
c = float(input('Nhập độ dài cạnh đáy :'))

x = b - c
if a*a + b*b == c*c :
    S = a*b/2
    print('Diện tích tam giác vuông là :' + str(S) + 'cm2')
if abs(x) < a < b + c :
    Cv = a + b + c
    print('Chu vi là ' + str(Cv) + 'cm')
else :
    print('Không là 3 cạnh 1 tam giác')