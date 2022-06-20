print('Nhập độ dài ba cạnh :')
a = float(input('Nhập độ dài cạnh bên :'))
b = float(input('Nhập độ dài cạnh bên :'))
c = float(input('Nhập độ dài cạnh đáy :'))

x = b - c
if abs(x) < a < b + c :
    Cv = a + b + c
    print('Chu vi là ' + str(Cv))
else :
    print('Không là 3 cạnh 1 tam giác')