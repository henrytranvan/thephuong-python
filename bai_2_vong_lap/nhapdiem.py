dsdiemtb = []
diem = 0 
stt = 0
while (diem <= 10) :
    diemtb = input('Nhập điểm ')
    stt = stt + 1
    if stt > 15 :
        break
    if (float(diemtb) <= 10) :
        dsdiemtb.append(float(diemtb))
    else : 
        break
x = 0
y = 0 
z = 0
t = 0
for i in dsdiemtb :
    if i >= 8.5 :
        x = x + 1  
    if 6.5 < i < 8.5 :
        y = y + 1
    if 5.0 < i  < 6.5 :
        z = z + 1
    if i <= 5 :
        t = t + 1
print('số hsg là ' + str(x))
print('số khá là ' + str(y))
print('số tb là ' + str(z))
print('số yếu là ' + str(t))

