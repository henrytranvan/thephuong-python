def solonhat2(l) :
    max= l[0]
    for i in range(1,len(l)) :
        if max < l[i] :
            max = l[i] 
    return max
print('Nhap 1 mang cac so')
ketthuc = False
ds = []
a = input()
while (a != 'k') :
    ds.append(float(a))
    a = input()


print(str(solonhat2(ds)))
