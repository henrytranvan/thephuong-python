a = float(input('Hãy nhập thời gian một công việc bằng giây :'))
while a < 0:
    print('Không thể nhận thời gian là số âm')
    a = float(input('Hãy nhập thời gian một công việc bằng giây :'))
x = a*60
y = a*3600
print(str(a) + 'giây' + '=' + str(x) + 'giờ')
print(str(a) + 'giây' + '=' + str(y) + 'phút')

