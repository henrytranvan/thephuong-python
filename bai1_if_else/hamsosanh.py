def sosanh(a,b) :
    if a > b : 
        return 'a la so lon hon'
    elif a == b :
        return 'a bang b'
    else :
        return 'b la so lon hon' 

print('nhap hai so a b')
a = float(input('nhap so a'))
b = float(input('nhap so b'))
ketqua = sosanh(a, b)
print('ket qua la ' + ketqua)


